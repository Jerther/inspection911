from odoo import fields, models


class Make(models.Model):
    _name = 'inspection911.make'
    name = fields.Char(required=True)
    brand_id = fields.Many2one('inspection911.brand', string="Brand", required=True, ondelete='cascade')
