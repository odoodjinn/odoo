# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError


class MaterialRequest(models.Model):
    _name = 'material.request'
    _description = 'Material Request Management'

    name = fields.Char(readonly=1, string='Sequence')
    partner_id = fields.Many2one('res.partner', string='Employee', required=True)
    date = fields.Date()
    material_ids = fields.One2many('material.order.line', 'material_id', string='Material Order Lines')
    state = fields.Selection([('draft', 'Draft'), ('approval', 'Approval'),
                              ('secondary_approval', 'Secondary Approval'), ('approved', 'Approved'),
                              ('rejected', 'Rejected')], default='draft')
    order_count = fields.Integer(string='Purchase Order Count', compute='_compute_purchase_order_count')
    transfer_count = fields.Integer(string='Internal Transfer Count', compute='_compute_internal_transfer_count')

    def _compute_purchase_order_count(self):
        """To display the count of purchase orders in smart button"""
        for rec in self:
            rec.order_count = self.env['purchase.order'].search_count([
                ('material_id', '=', self.id)
            ])

    def _compute_internal_transfer_count(self):
        """To display the count of internal transfers in smart button"""
        for rec in self:
            rec.transfer_count = self.env['stock.picking'].search_count([
                ('origin', '=', self.id)
            ])

    @api.model_create_multi
    def create(self, vals_list):
        """Function to create sequence numbers for Material request records"""
        sequences = super().create(vals_list)
        for rec in sequences:
            rec['name'] = self.env['ir.sequence'].next_by_code('material_sequence_code')
        return sequences

    def action_submit(self):
        """Submit button to change the state draft to approval state for users"""
        vendors = self.material_ids.product_id.seller_ids.mapped('partner_id')
        if vendors:
            self.state = 'approval'
        else:
            raise UserError('There is no vendor for the product selected for purchase')

    def action_approve(self):
        """Approve button to change the state approval to secondary approval state for managers"""
        self.state = 'secondary_approval'

    def action_head_reject(self):
        """Head reject button to change the state secondary approval to rejected state for head"""
        self.state = 'rejected'

    def action_head_approve(self):
        """Head approve button action to check the order lines and create the
        purchase order/internal transfer based on the type and change the state to approved"""
        self.state = 'approved'
        for rec in self.material_ids:
            vendors = rec.product_id.seller_ids.mapped('partner_id')
            if rec.type == 'purchase':
                lines = []
                order_line_values = {
                    'name': rec.product_id.name,
                    'product_id': rec.product_id.id,
                    'product_qty': rec.quantity,
                    'price_unit': rec.product_id.standard_price,
                    'price_subtotal': rec.total_price
                }
                lines.append(fields.Command.create(order_line_values))
                if lines:
                    for record in vendors:
                        order_values = {
                            'partner_id': record.id,
                            'order_line': lines,
                            'material_id': self.id
                        }
                        self.env['purchase.order'].create(order_values)

            else:
                lines = []
                warehouse = self.env['stock.warehouse'].search([('company_id', '=', self.env.company.id)], limit=1)
                stock_location = warehouse.lot_stock_id
                order_line_values = {
                    'name': rec.product_id.name,
                    'product_id': rec.product_id.id,
                    'product_uom_qty': rec.quantity,
                    'location_id': stock_location.id,
                    'location_dest_id': stock_location.id,
                }
                lines.append(fields.Command.create(order_line_values))
                if lines:
                    order_values = {
                        'partner_id': self.partner_id.id,
                        'picking_type_id': self.env.ref('stock.picking_type_internal').id,
                        'move_ids': lines,
                        'origin': self.id,
                    }
                    self.env['stock.picking'].create(order_values)

    def action_purchase_order(self):
        """Click action of purchase order smart button"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'res_model': 'purchase.order',
            'domain': [('material_id', '=', self.id)]
        }

    def action_internal_transfer(self):
        """Click action of internal transfer smart button"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Internal Transfers',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('origin', '=', self.id)],
        }


# class MaterialOrderLine(models.Model):
#     _name = 'material.order.line'
#     _description = 'Material Order Lines'
#
#     material_id = fields.Many2one('material.request', string='Material')
#     product_id = fields.Many2one('product.product', string='Product')
#     quantity = fields.Integer(string='Quantity', default=1)
#     total_price = fields.Image(string='Total Price')
#     type = fields.Selection([('purchase', 'Purchase Order'), ('internal', 'Internal Transfer')], default='purchase')


# class PurchaseOrder(models.Model):
#     _inherit = 'purchase.order'
#
#     material_id = fields.Many2one('material.management', string='Material')


# class StockPicking(models.Model):
#     _inherit = 'stock.picking'
#
#     material_id = fields.Many2one('material.management', string='Material')
