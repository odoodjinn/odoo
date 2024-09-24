# -*- coding: utf-8 -*-

from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    extra_cost_ids = fields.One2many('extra.cost.line', 'extra_cost_id', string='Extra Cost')
    bill_count = fields.Integer(string='Bill Count', compute='_compute_bill_count')

    def action_create_cost_bill(self):
        lines = []
        for rec in self.move_raw_ids:
            if rec.picked:
                line_values = {
                    'product_id': rec.product_id.id,
                    'name': rec.product_id.name,
                    'quantity': rec.product_uom_qty,
                    'price_unit': rec.component_cost,
                }
                lines.append(fields.Command.create(line_values))
        for record in self.extra_cost_ids:
            extra_line_values = {
                'name': record.description,
                'price_unit': record.cost,
            }
            lines.append(fields.Command.create(extra_line_values))
        if lines:
            bill_values = {
                'move_type': 'in_invoice',
                'invoice_date': fields.Date.today(),
                'mo_id': self.id,
                'invoice_line_ids': lines
            }
            vendor_bill = self.env['account.move'].create(bill_values)
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_type': 'tree,form',
                'view_mode': 'form',
                'res_id': vendor_bill.id,
                'view_id': (self.env.ref('account.view_move_form').id, 'form'),
            }

    def action_vendor_bill(self):
        """Click action of purchase order smart button"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vendor Bills',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'res_model': 'account.move',
            'domain': [('mo_id', '=', self.id)]
        }
    
    def _compute_bill_count(self):
        """To display the count of purchase orders in smart button"""
        for rec in self:
            rec.bill_count = self.env['account.move'].search_count([
                ('mo_id', '=', self.id)
            ])

