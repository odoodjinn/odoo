# -*- coding: utf-8 -*-

from odoo import fields, models


class ExtraCostLine(models.Model):
    _name = 'extra.cost.line'
    _description = 'Extra Cost Line'

    extra_cost_id = fields.Many2one('mrp.production', string='Extra Cost')
    description = fields.Char(string='Description')
    cost = fields.Float(string='Cost')