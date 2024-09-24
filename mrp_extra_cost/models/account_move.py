# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    mo_id = fields.Many2one('mrp.production', string='Manufacturing Order')