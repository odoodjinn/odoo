# -*- coding: utf-8 -*-

from odoo import api, fields,models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_name_es = fields.Char(string='Product Name in Spanish', compute='translate_product_name', readonly=True)

    @api.depends('name')
    def translate_product_name(self):
        for rec in self:
            rec.product_name_es = rec.with_context(lang='es_ES').name
