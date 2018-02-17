from odoo import fields, models


class FireStation(models.Model):
    _name = 'fire_station'
    name = fields.Char(required=True)
    fireman_ids = fields.Many2many('fireman', 'fire_station_fireman_rel', string='Firemen')
