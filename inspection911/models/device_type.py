from odoo import fields, models


class DeviceType(models.Model):
    _name = 'device_type'
    name = fields.Char(required=True)
    device_ids = fields.One2many('device', 'type_id', string="Devices")
