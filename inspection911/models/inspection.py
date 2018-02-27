from odoo import fields, models


class Inspection(models.Model):
    _name = 'inspection'
    fire_station_id = fields.Many2one('fire_station', "Fire Station", required=True, ondelete='cascade')
    device_id = fields.Many2one('device', "Device", required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', "User", required=True, ondelete='cascade')
    complies = fields.Boolean()
    comment = fields.Html()
    date = fields.Datetime(required=True, default=fields.Datetime.now())
