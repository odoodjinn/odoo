# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    component_cost = fields.Float(string='Component Cost', related='product_id.standard_price')

    # @api.depends('product_id')
    # def _compute_component_cost(self):
    #     for rec in self:
    #         rec.component_cost = rec.product_id.standard_price