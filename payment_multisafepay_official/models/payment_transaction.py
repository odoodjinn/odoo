# -*- coding: utf-8 -*-

import logging
import pprint
from ast import parse

from werkzeug import urls

from odoo import _, models
from odoo.exceptions import ValidationError
from ..controllers.main import MultiSafePayController


_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """Redirects to the payment page"""
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res
        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s", pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request(data=payload, method='POST')
        print(payment_data, '>>payment data')
        self.provider_reference = payment_data['data']['order_id']
        checkout_url = payment_data['data']['payment_url']
        print(checkout_url, '>>checkout url')
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        print(parsed_url, '>>parsed url')
        print(url_params, '>>decode url')
        return {'api_url': checkout_url, 'url_params': url_params}

    def _multisafepay_prepare_payment_request_payload(self):
        """Prepare the data to be sent to the payment website"""
        user_lang = self.env.context.get('lang')
        base_url = self.provider_id.get_base_url()
        redirect_url = urls.url_join(base_url, MultiSafePayController._return_url)
        print(self.search_read([], limit=1), '>>self search_read')
        return {
          "type": "redirect",
          "order_id": f"my-order-id-{self.id}",
          "gateway": "",
          "currency": self.currency_id.name,
          "amount": self.amount*100,
          "description": "Test order description",
          "payment_options": {
            'redirect_url': f'{redirect_url}?ref={self.reference}',
            "close_window": True
          },
          "customer": {
            "locale": user_lang,
            "ip_address": "123.123.123.123",
            "first_name": self.partner_name,
            "company_name": self.company_id.name,
            "address1": self.partner_address,
            "zip_code": self.partner_zip,
            "city": self.partner_city,
            "country": self.partner_country_id.name,
            "phone": self.partner_phone,
            "email": self.partner_email,
            "referrer": "https://example.com",
            "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
            }
        }

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        """ Override of payment to find the transaction based on MultiSafePay data.

               :param str provider_code: The code of the provider that handled the transaction
               :param dict notification_data: The notification data sent by the provider
               :return: The transaction if found
               :rtype: recordset of `payment.transaction`
               :raise: ValidationError if the data match no transaction
               """
        tx = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != 'multisafepay' or len(tx) == 1:
            return tx

        tx = self.search(
            [('reference', '=', notification_data.get('ref')), ('provider_code', '=', 'multisafepay')]
        )
        if not tx:
            raise ValidationError("MultiSafePay: " + _(
                "No transaction found matching reference %s.", notification_data.get('ref')
            ))
        return tx

    def _process_notification_data(self, notification_data):
        """ Override of payment to process the transaction based on MultiSafePay data.

        Note: self.ensure_one()

        :param dict notification_data: The notification data sent by the provider
        :return: None
        """
        super()._process_notification_data(notification_data)
        if self.provider_code != 'multisafepay':
            return
        print(notification_data, '>>>notification data')
        transaction_id = notification_data['transactionid']
        payment_data = self.provider_id._multisafepay_make_request(data=transaction_id, method='GET')
        payment_status = payment_data['data']['status']
        print(payment_data, '>>Dataaa')
        print(payment_status, '>>status')

        if payment_status in ['initialized', 'uncleared']:
            self._set_pending()
        elif payment_status in ['completed', 'shipped']:
            self._set_done()
        elif payment_status in ['void', 'cancel', 'declined']:
            self._set_canceled("MultiSafePay: " + _("Canceled payment with status: %s", payment_status))
        else:
            self._set_error('Error')
