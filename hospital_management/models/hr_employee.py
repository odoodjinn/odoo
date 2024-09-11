from odoo import models, fields


class Employee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer('Age')
    dob = fields.Date('Date of Birth')
    fees = fields.Integer('Fees')
    qualification = fields.Char('Qualification')
