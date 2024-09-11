from odoo import models, fields

class RealEstate(models.Model):
    _name = "real_estate"
    _description = "Real Estate"

    name = fields.Char('Name')


