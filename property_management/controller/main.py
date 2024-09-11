# -*- coding: utf-8 -*-

import json
from odoo import fields, http
from odoo.http import content_disposition, request, Controller, route
from odoo.http import serialize_exception as _serialize_exception
from odoo.tools import html_escape

class XLSXReportController(http.Controller):
    """XlsxReport generating controller"""
    @http.route('/xlsx_reports', type='http', auth='user', methods=['POST'], csrf=False)
    def get_report_xlsx(self, model, options, output_format, **kw):
        """
        Generate an XLSX report based on the provided data and return it as a
        response.
        """
        uid = request.session.uid
        report_obj = request.env[model].with_user(uid)
        options = json.loads(options)
        token = 'dummy-because-api-expects-one'
        try:
            if output_format == 'xlsx':
                response = request.make_response(
                    None,
                    headers=[
                        ('Content-Type', 'application/vnd.ms-excel'),
                        ('Content-Disposition',
                         content_disposition('Rental/Lease Excel Report' + '.xlsx'))
                    ]
                )
                report_obj.get_xlsx_report(options, response)
                response.set_cookie('fileToken', token)
                return response
        except Exception as e:
            se = _serialize_exception(e)
            error = {
                'code': 200,
                'message': 'Odoo Server Error',
                'data': se
            }
            return request.make_response(html_escape(json.dumps(error)))


class WebFormController(Controller):
    @route('/property_details', type='http', auth='public', website=True)
    def property_form(self, **kwargs):
        state_rec = request.env['res.country.state'].sudo().search([])
        country_rec = request.env['res.country'].sudo().search([])
        owner_rec = request.env['res.partner'].sudo().search([])
        facility_rec = request.env['property.facility'].sudo().search([])
        return request.render('property_management.property_web_form_template', {
            "state_rec": state_rec,
            "country_rec": country_rec,
            "owner_rec": owner_rec,
            "facility_rec": facility_rec,
        })

    @route('/property_details/submit', type='http', auth='public', website=True, methods=['GET', 'POST'])
    def property_form_submit(self, **post):
        request.env['property.details'].sudo().create({
                    'name': post.get('name'),
                    'street': post.get('street'),
                    'street2': post.get('street2'),
                    'city': post.get('city'),
                    'zip': post.get('zip'),
                    'state_id': post.get('state_id'),
                    'country_id': post.get('country_id'),
                    'owner_id': post.get('owner_id'),
                    'can_be_sold': post.get('can_be_sold'),
                    'rent': post.get('rent'),
                    'built_date': post.get('built_date'),
                    'legal_amount': post.get('legal_amount'),
                    'facility_ids': post.get('facility_ids'),
                    'description': post.get('description'),
                })
        return request.render('property_management.property_web_form_success')

    @route('/management', type='http', auth='public', website=True)
    def rental_lease_form(self, **kwargs):
        partner_rec = request.env['res.partner'].sudo().search([])
        property_rec = request.env['property.details'].sudo().search([])
        company_rec = request.env['res.company'].sudo().search([])
        return request.render('property_management.rental_lease_web_form_template', {
            'partner_rec': partner_rec,
            'property_rec': property_rec,
            'company_rec': company_rec,
        })

    @route('/management/submit', type='http', auth='public', website=True, methods=['GET', 'POST'])
    def rental_lease_form_submit(self, **post):
        request.env['rental.lease.management'].create({
            'tenant_id': post.get('tenant_id'),
            'due_date': post.get('due_date'),
            'company_id': post.get('company_id'),
            'type': post.get('type'),
            'property_ids':[fields.Command.create({
                'property_id': post.get('property_id'),
                'owner_id': post.get('owner_id'),
                'start_date': post.get('start_date'),
                'end_date': post.get('end_date'),
                'total_days': post.get('total_days'),
                'rent_lease_amount': post.get('rent_lease_amount'),
                'total_amount': post.get('total_amount'),
            })]
        })
        return request.render('property_management.rental_lease_web_form_success')
