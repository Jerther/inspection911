from odoo import fields, models


class Brand(models.Model):
    _name = 'brand'
    name = fields.Char(required=True)
    make_ids = fields.One2many('make', 'brand_id', string="Makes")
