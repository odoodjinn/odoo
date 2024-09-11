from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char('Property Name', required=True, translate=True)
    expected_price = fields.Float('Expected price')
    selling_price = fields.Float('Selling price', readonly=True, copy=False)
    availability_date = fields.Date('Available from', copy=False, default=fields.Date.today())
    bedrooms = fields.Integer(default=2)
    active = fields.Boolean(default=True)
    garage = fields.Boolean()
    garden = fields.Boolean()
    state = fields.Selection([('option1', 'New'), ('option2', 'Offer Received'), ('option3', 'Offer Accepted'), ('option4', 'Sold'), ('option5', 'Cancelled')], default='option1')
    postcode = fields.Char()
    living_area = fields.Integer('Living Area (sqm)')
    garden_area = fields.Integer('Garden Area (sqm)')
    description = fields.Text()
    facades = fields.Integer()
