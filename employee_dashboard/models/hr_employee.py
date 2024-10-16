# -*- coding: utf-8 -*-
from datetime import date

from odoo import api, fields, models
from odoo.tools.safe_eval import dateutil


class CrmLead(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def get_tiles_data(self):
        """ Return the tile data"""
        user_id = self.env.user
        employee_data = self.env['hr.employee'].sudo().search([])
        employee_attendance = self.env['hr.attendance'].sudo().search([])
        employee_leave = self.env['hr.leave'].sudo().search([])
        employee_project = self.env['project.project'].sudo().search([])
        employee_self = employee_data.filtered(lambda x: x.user_id == user_id)
        attendance = employee_attendance.filtered(lambda x: x.employee_id.user_id == user_id)
        leave = employee_leave.filtered(lambda x: x.employee_id.user_id == user_id)
        project = employee_project.filtered(lambda x: x.user_id == user_id)
        today = fields.Datetime.today()
        experience = (today-employee_self.create_date).days/365
        # groups = self.env['res.groups'].search([])
        # user_group = groups.filtered(lambda x: x.users in user_id)
        # for rec in user_group:
        #     print(rec.name)
        # print(groups,'//grp')
        # print(user_group,'//ugrp')
        employee_info = {
            'id': employee_self.id,
            'name': employee_self.name,
            'position': employee_self.job_id.name,
            'department': employee_self.department_id.name,
            'experience': int(experience),
        }
        return {
            'user_id': user_id,
            'total_employee': len(employee_data),
            'total_attendance': len(attendance),
            'total_leave': len(leave),
            'total_project': len(project),
            'employee_info': employee_info,
        }
