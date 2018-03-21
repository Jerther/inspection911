from odoo import api, fields, models
from odoo.http import request


class Inspection(models.Model):
    _name = 'inspection'
    _rec_name = 'device_id'

    user_id = fields.Many2one('res.users', "User", required=True, ondelete='cascade', default=lambda self: self.env.user.id)
    device_id = fields.Many2one('device', "Device", required=True, ondelete='cascade')
    complies = fields.Boolean(default=True)
    comment = fields.Html()
    date = fields.Datetime(required=True, default=fields.Datetime.now())
    location_id = fields.Many2one('location', "Location", required=True, ondelete='cascade')

    def _default_device_type_id(self):
        return request.session.device_type_id or \
               self.env['device_type'].search([], limit=1)

    device_type_id = fields.Many2one('device_type', "Device type", store=False, default=_default_device_type_id)

    def _fire_station_id_domain(self):
        ids = [s.id for s in self.env.user.fire_station_ids]
        return [('id', 'in', ids)]

    def _default_fire_station_id(self):
        return request.session.fire_station_id or \
               self.env['fire_station'].search(self._fire_station_id_domain(), limit=1)

    fire_station_id = fields.Many2one('fire_station', "Fire Station", domain=_fire_station_id_domain,
                                      default=_default_fire_station_id, required=True, ondelete='cascade')

    @api.onchange('fire_station_id')
    def onchange_fire_station_id(self):
        ids = [l.id for l in self.fire_station_id.location_ids]
        location_domain = [('id', 'in', ids)]
        request.session.fire_station_id = self.fire_station_id.id
        if request.session.location_id and request.session.location_id in [l.id for l in self.fire_station_id.location_ids]:
            location_id = request.session.location_id
        else:
            location_id = self.env['location'].search(location_domain, limit=1)
        return {
            'domain': {'location_id': location_domain},
            'value': {'location_id': location_id}
        }

    @api.onchange('location_id')
    def onchange_location_id(self):
        request.session.location_id = self.location_id.id
        ids = [d.id for d in self.location_id.device_ids]
        if self.device_type_id:
            ids = [i for i in ids if i in [d.id for d in self.device_type_id.device_ids]]
        return {
            'domain': {'device_id': [('id', 'in', ids)]},
            'value': {'device_id': False}
        }

    @api.onchange('device_type_id')
    def onchange_device_type_id(self):
        request.session.device_type_id = self.device_type_id.id
        ids = [d.id for d in self.location_id.device_ids]
        if self.device_type_id:
            ids = [i for i in ids if i in [d.id for d in self.device_type_id.device_ids]]
        return {
            'domain': {'device_id': [('id', 'in', ids)]},
            'value': {'device_id': False}
        }
