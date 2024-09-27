# -*- coding: utf-8 -*-

import logging
import pprint

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request

_logger = logging.getLogger(__name__)


class MultiSafePayController(http.Controller):
    _return_url = '/payment/multisafepay/return'
    _webhook_url = '/payment/multisafepay/webhook'

    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'], csrf=False,
        save_session=False
    )
    def multisafepay_return_from_checkout(self, **data):

        _logger.info("handling redirection from MultiSafePay with data:\n%s", pprint.pformat(data))
        # request.env['payment.transaction'].sudo()._handle_notification_data('multisafepay', data)
        return request.redirect('/payment/status')
