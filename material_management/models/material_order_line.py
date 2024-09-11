# -*- coding: utf-8 -*-

from odoo import fields, models


class MaterialOrderLine(models.Model):
    _name = 'material.order.line'
    _description = 'Material Order Lines'

    material_id = fields.Many2one('material.request', string='Material')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Integer(string='Quantity', default=1)
    total_price = fields.Image(string='Total Price')
    type = fields.Selection([('purchase', 'Purchase Order'), ('internal', 'Internal Transfer')], default='purchase')