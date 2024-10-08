# -*- coding: utf-8 -*-

from odoo import api, models


class OwlModel(models.Model):
    _name = 'owl.model'
    _description = 'Owl Model'

    @api.model
    def owl_model_function(self):
        return self.env['sale.order'].search([], limit=10)