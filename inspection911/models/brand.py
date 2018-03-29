from odoo import fields, models


class Brand(models.Model):
    _name = 'inspection911.brand'
    name = fields.Char(required=True)
    make_ids = fields.One2many('inspection911.make', 'brand_id', string="Makes")
