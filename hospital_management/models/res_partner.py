from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer('Age')
    dob = fields.Date('Date of Birth')
    blood_group = fields.Selection([('op1', 'A+'), ('op2', 'B+'), ('op3', 'O+'), ('op4', 'AB+'), ('op5', 'A-'), ('op6', 'B-'), ('op6', 'O-'), ('op7', 'AB-')])
