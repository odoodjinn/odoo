# -*- coding: utf-8 -*-
from datetime import date, datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class HrAttendanceDailyReport(models.AbstractModel):
    _name = 'report.hr_attendance_daily.report_hr_attendance_daily'
    _description = 'Daily Attendance Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        """ Fetch data from the wizard model and attendance model,
        and then return to the qweb template to print the pdf."""
        attendance_obj = self.env['hr.attendance'].search([
            ('check_in', '>=', data['start_date']),
            # ('check_out', '<=', data['end_date']),
        ])
        print(data, '//data')
        if not attendance_obj:
            raise ValidationError('No such records found!')
        return {
            'docs': attendance_obj,
        }
