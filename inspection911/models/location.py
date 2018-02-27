from odoo import fields, models


class Location(models.Model):
    _name = 'location'
    name = fields.Char(required=True)
    fire_station_id = fields.Many2one('fire_station', "Fire Station", required=True, ondelete='cascade')
    device_ids = fields.Many2many('device', 'location_device_rel', string="Devices")
