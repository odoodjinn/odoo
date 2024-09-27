# -*- coding: utf-8 -*-

import logging
import pprint
import requests

from odoo import _, fields, models, service
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[("multisafepay", "MultiSafePay")],
        ondelete={"multisafepay": "set default"},
    )
    multisafepay_api_key = fields.Char('MultiSafePay test api key', size=40)

    def _multisafepay_make_request(self, data=None, method='POST'):
        self.ensure_one()
        url = f'https://testapi.multisafepay.com/v1/json/orders?api_key={self.multisafepay_api_key}'
        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        try:
            response = requests.request(method, url, json=data, headers=headers, timeout=60)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                _logger.exception(
                    "Invalid API request at %s with data:\n%s", url, pprint.pformat(data)
                )
                raise ValidationError(
                    "MultiSafePay: " + _(
                        "The communication with the API failed. Mollie gave us the following "
                        "information: %s", response.json().get('detail', '')
                    ))
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            _logger.exception("Unable to reach endpoint at %s", url)
            raise ValidationError(
                "MultiSafePay: " + _("Could not establish the connection to the API.")
            )
        return response.json()