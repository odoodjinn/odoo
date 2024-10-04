# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('to_approve', 'To Approve'), ('secondary_approval', 'Secondary Approval'), ('sent',)])
    primary_user = fields.Many2one('res.users', compute='_compute_primary_user')
    current_user = fields.Many2one('res.users', compute='_compute_primary_user')

    @api.depends('primary_user', 'current_user')
    def _compute_primary_user(self):
        user_check = self.env['res.config.settings'].search([])
        for rec in self:
            rec.primary_user = user_check.primary_user
            rec.current_user = self.env.user

    def _can_be_confirmed(self):
        self.ensure_one()
        return self.state in {'draft', 'sent', 'secondary_approval'}
    
    def action_confirm(self):
        if (self.amount_total > 25000) and (self.state not in ['to_approve', 'secondary_approval']):
            self.state = 'to_approve'
            return
        return super(SaleOrder, self).action_confirm()

    def action_approve(self):
        # self.state = 'secondary_approval'
        user_check = self.env['res.config.settings'].search([])
        print(user_check.primary_user.name, '//user')
        print(user_check.secondary_user.name, '//user2')
        print(self.primary_user, '//primary')
        print(self.current_user, '//current user')
        print(self.env.user, '//')

    def action_second_approve(self):
        self.action_confirm()