from odoo import fields, models


class Fireman(models.Model):
    _name = 'fireman'
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    fire_station_ids = fields.Many2many('fire_station', 'fire_station_fireman_rel', string='Fire Stations')
