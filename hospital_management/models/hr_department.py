from odoo import models, fields


class Department(models.Model):
    _inherit = "hr.department"

    block = fields.Char()