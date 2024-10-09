# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.http import request


class CrmLead(models.Model):
    _inherit = 'hr.employee'
    @api.model
    def get_tiles_data(self):
        """ Return the tile data"""
        employee_data = self.env['hr.employee'].search([])
        print(request.session.uid)
        for rec in employee_data:
            print(rec.user_id,'//data userid')
        # company_id = self.env.company
        # leads = self.search([('company_id', '=', self.env.company.id),
        #                      ('user_id', '=', self.env.user.id)])
        # my_leads = leads.filtered(lambda r: r.type == 'lead')
        # my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        # currency = company_id.currency_id.symbol
        # expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
        return {
            'total_employee': len(employee_data),
            # 'total_leads': len(my_leads),
            # 'total_opportunity': len(my_opportunity),
            # 'expected_revenue': expected_revenue,
            # 'currency': currency,
        }
