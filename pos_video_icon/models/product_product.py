# -*- coding: utf-8 -*-

from odoo import api, fields, models
# from odoo.addons.web_editor.tools import get_video_embed_code


class ProductProduct(models.Model):
    _inherit = 'product.product'

    video_url = fields.Char(string='Video URL')
