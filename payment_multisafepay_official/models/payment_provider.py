# -*- coding: utf-8 -*-

import requests
from odoo import _, fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[("multisafepay", "MultiSafePay")],
        ondelete={"multisafepay": "set default"},
    )
    multisafepay_api_key = fields.Char('MultiSafePay test api key', size=40)

    def _multisafepay_make_request(self, data=None, method=None):
        """Function definition to create request to the MultiSafePay website"""
        self.ensure_one()
        if method == 'POST':
            url = f'https://testapi.multisafepay.com/v1/json/orders?api_key={self.multisafepay_api_key}'
            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
            }
            response = requests.request(method, url, json=data, headers=headers, timeout=60)
            return response.json()
        else:
            url = f'https://testapi.multisafepay.com/v1/json/orders/{data}/?api_key={self.multisafepay_api_key}'
            headers = {
                'accept': 'application/json',
            }
            response = requests.request(method, url, headers=headers, timeout=60)
            return response.json()
