# -*- coding: utf-8 -*-

import logging
import pprint

from werkzeug import urls

from odoo import _, models
from ..controllers.main import MultiSafePayController


_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res

        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s", pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request(data=payload)
        self.provider_reference = payment_data.get('id')

        checkout_url = payment_data['data']['payment_url']
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        return {'api_url': checkout_url, 'url_params': url_params}

    def _multisafepay_prepare_payment_request_payload(self):
        user_lang = self.env.context.get('lang')
        base_url = self.provider_id.get_base_url()
        redirect_url = urls.url_join(base_url, MultiSafePayController._return_url)
        webhook_url = urls.url_join(base_url, MultiSafePayController._webhook_url)
        print(self.search_read([], limit=1))
        print(f'{redirect_url}?ref={self.reference}','kkkkk')
        print(redirect_url,'redirect')
        print(base_url,'base')
        return {
          "type": "redirect",
          "order_id": f"my-order-id-{self.id}",
          "gateway": "",
          "currency": self.currency_id.name,
          "amount": self.amount,
          "description": "Test order description",
          "payment_options": {
            "notification_url": "https://www.example.com/client/notification?type=notification",
            "notification_method": "POST",
            'redirectUrl': f'{redirect_url}?ref={self.reference}',
            "cancel_url": "https://www.example.com/client/notification?type=cancel",
            "close_window": True
          },
          "customer": {
            "locale": self.partner_lang,
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