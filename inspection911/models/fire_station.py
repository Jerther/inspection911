from odoo import fields, models


class FireStation(models.Model):
    _name = 'fire_station'
    name = fields.Char(required=True)
    user_ids = fields.Many2many('res.users', 'fire_station_users_rel', string='Users')
    location_ids = fields.One2many('location', 'fire_station_id', string="Locations", domain=['|', ('active', '=', False), ('active', '=', True)]) #context active_test False semble pas marcher.
