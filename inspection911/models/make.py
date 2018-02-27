from odoo import fields, models


class Make(models.Model):
    _name = 'make'
    name = fields.Char(required=True)
    brand_id = fields.Many2one('brand', string="Brand", required=True, ondelete='cascade')
