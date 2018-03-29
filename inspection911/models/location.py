from odoo import fields, models


class Location(models.Model):
    _name = 'inspection911.location'
    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    fire_station_id = fields.Many2one('inspection911.fire_station', "Fire Station", required=True, ondelete='cascade')
    device_ids = fields.Many2many('inspection911.device', 'location_device_rel', string="Devices")
