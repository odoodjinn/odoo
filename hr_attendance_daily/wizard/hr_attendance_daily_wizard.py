# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.tools import date_utils


class HrAttendanceDailyWizard(models.TransientModel):
    _name = 'hr.attendance.daily.wizard'
    _description = 'Daily Attendance Report Wizard'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    print_by = fields.Selection([('daily', 'Daily'),('weekly', 'Weekly'), ('monthly', 'Monthly')])

    def action_print_report(self):
        """Print button action on the wizard to pass the filter data to the abstract model
            and print the pdf"""
        start_date = self.start_date
        starting_week = date_utils.start_of(start_date, "week")
        print(starting_week, 'starting week')
        data = {
            'start_date': start_date,
            'end_date': self.end_date,
            'print_by': self.print_by,
        }
        return self.env.ref('hr_attendance_daily.action_report_hr_attendance_daily').report_action(
            None, data=data)
