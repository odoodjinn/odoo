# -*- coding: utf-8 -*-

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    material_id = fields.Many2one('material.management', string='Material')
