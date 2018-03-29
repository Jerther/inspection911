from odoo import fields, models


class DeviceType(models.Model):
    _name = 'inspection911.device_type'
    name = fields.Char(required=True)
    device_ids = fields.One2many('inspection911.device', 'type_id', string="Devices")
