# -*- coding: utf-8 -*-

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request, Controller, route

class PortalAccount(CustomerPortal):
   def _prepare_home_portal_values(self, counters):
       """To get the Manufacturing Orders in the website portal"""
       values = super()._prepare_home_portal_values(counters)
       mo_count = request.env['mrp.production'].search_count([])
       values['mo_count'] = mo_count
       return values

   @route('/my/mo', type='http', auth='public', website=True)
   def manufacturing_order_portal(self):
       """Displaying Manufacturing orders based on customer field"""
       user = request.env.user
       mo_rec = request.env['mrp.production'].sudo().search([('partner_id', '=', user.partner_id.id)])
       return request.render('website_mo.mo_customer_portal_template', {
           'mo_rec': mo_rec,
       })
