from odoo import api, fields, models


class Inspection(models.Model):
    _name = 'inspection'
    _rec_name = 'device_id'

    user_id = fields.Many2one('res.users', "User", required=True, ondelete='cascade', default=lambda self: self.env.user.id)
    device_id = fields.Many2one('device', "Device", required=True, ondelete='cascade')
    location_id = fields.Many2one('location', "Location", required=True, ondelete='cascade')
    complies = fields.Boolean()
    comment = fields.Html()
    date = fields.Datetime(required=True, default=fields.Datetime.now())

    def _fire_station_id_domain(self):
        ids = [s.id for s in self.env.user.fire_station_ids]
        return [('id', 'in', ids)]

    fire_station_id = fields.Many2one('fire_station', "Fire Station", domain=_fire_station_id_domain, required=True, ondelete='cascade')

    @api.onchange('fire_station_id')
    def onchange_fire_station_id(self):
        ids = [l.id for l in self.fire_station_id.location_ids]
        return {
            'domain': {'location_id': [('id', 'in', ids)]},
            'value': {'location_id': False}
        }

    @api.onchange('location_id')
    def onchange_location_id(self):
        ids = [d.id for d in self.location_id.device_ids]
        return {
            'domain': {'device_id': [('id', 'in', ids)]},
            'value': {'device_id': False}
        }
