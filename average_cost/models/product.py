# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    average_cost = fields.Float(string='Average Cost', compute="_compute_average_cost")

    def _compute_average_cost(self):
        purchase_order_line = self.env['purchase.order.line'].search([('product_id', '=', self.id)])
        total = sum(purchase_order_line.mapped('price_unit'))
        self.average_cost = total/len(purchase_order_line)

