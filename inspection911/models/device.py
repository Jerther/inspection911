from odoo import fields, models


class Device(models.Model):
    _name = 'device'
    uid = fields.Char(required=True)
