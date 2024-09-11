# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_ids = fields.Many2many('sale.order', string='Related SO')

    @api.onchange('sale_order_ids')
    def _onchange_sale_order(self):
        """Adding invoice lines based on the sale orders selected through related SO field"""
        if self.sale_order_ids:
            for rec in self.sale_order_ids.order_line:
                existing_product = self.invoice_line_ids.filtered(lambda x: x.product_id == rec.product_id)
                if existing_product:
                    # qty = existing_product.mapped('quantity')
                    # qty += rec.product_uom_qty
                    for record in existing_product:
                        if record.quantity != rec.product_uom_qty:
                            record.quantity += rec.product_uom_qty
                else:
                    self.invoice_line_ids = [fields.Command.create({
                            'product_id': rec.product_id.id,
                            'name': rec.product_id.name,
                            'price_unit': rec.price_unit,
                            'quantity': rec.product_uom_qty,

                    })]
        else:
            self.invoice_line_ids = fields.Command.clear()

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        """Clearing selection of related SO field when partner is changed"""
        self.sale_order_ids = False
