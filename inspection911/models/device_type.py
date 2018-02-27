from odoo import fields, models


class DeviceCategory(models.Model):
    name = fields.Char(required=True)
    device_ids = fields.One2many('device', 'category_id', string="Devices")