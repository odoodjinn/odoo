# -*- coding: utf-8 -*-

import logging
import pprint

from werkzeug import urls

from odoo import _, models

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return MultiSafePay-specific rendering values.

        Note: self.ensure_one() from `_get_processing_values`

        :param dict processing_values: The generic and specific processing values of the transaction
        :return: The dict of provider-specific rendering values
        :rtype: dict
        """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res

        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s", pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('/payments', data=payload)

        # The provider reference is set now to allow fetching the payment status after redirection
        self.provider_reference = payment_data.get('id')

        # Extract the checkout URL from the payment data and add it with its query parameters to the
        # rendering values. Passing the query parameters separately is necessary to prevent them
        # from being stripped off when redirecting the user to the checkout URL, which can happen
        # when only one payment method is enabled on Mollie and query parameters are provided.
        checkout_url = payment_data['_links']['checkout']['href']
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        return {'api_url': checkout_url, 'url_params': url_params}

    def _multisafepay_prepare_payment_request_payload(self):
        """ Create the payload for the payment request based on the transaction values.

        :return: The request payload
        :rtype: dict
        """
        user_lang = self.env.context.get('lang')
        base_url = self.provider_id.get_base_url()
        # redirect_url = urls.url_join(base_url, MollieController._return_url)
        # webhook_url = urls.url_join(base_url, MollieController._webhook_url)
        # decimal_places = CURRENCY_MINOR_UNITS.get(
        #     self.currency_id.name, self.currency_id.decimal_places
        # )

        return {
            'description': self.reference,
            'amount': {
                'currency': 'EUR',
                # 'value': f"{self.amount:.{decimal_places}f}",
            },
            # 'locale': user_lang if user_lang in const.SUPPORTED_LOCALES else 'en_US',
            # 'method': [const.PAYMENT_METHODS_MAPPING.get(
            #     self.payment_method_code, self.payment_method_code
            # )],
            # Since Mollie does not provide the transaction reference when returning from
            # redirection, we include it in the redirect URL to be able to match the transaction.
            # 'redirectUrl': f'{redirect_url}?ref={self.reference}',
            # 'webhookUrl': f'{webhook_url}?ref={self.reference}',
        }