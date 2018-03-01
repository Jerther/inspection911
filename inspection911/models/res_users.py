from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'
    fire_station_ids = fields.Many2many('fire_station', 'fire_station_fireman_rel', string='Fire Stations')
    number = fields.Char(help="License number")
