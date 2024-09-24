# -*- coding: utf-8 -*-

from odoo import api, fields, models
# from odoo.addons.web_editor.tools import get_video_embed_code
# from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    video_url = fields.Char(string='Video URL')
    # embed_code = fields.Html(string='Video Preview', compute='_compute_embed_code')
    #
    # @api.depends('video_url')
    # def _compute_embed_code(self):
    #     for image in self:
    #         image.embed_code = get_video_embed_code(image.video_url)
    #
    # @api.constrains('video_url')
    # def _check_valid_video_url(self):
    #     for image in self:
    #         if image.video_url and not image.embed_code:
    #             raise ValidationError("Provided video URL for is not valid. Please enter a valid video URL.")

