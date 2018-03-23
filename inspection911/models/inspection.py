from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
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
        return request and \
               request.session.device_type_id or \
               self.env['device_type'].search([], limit=1)

    device_type_id = fields.Many2one('device_type', "Device type", store=False, default=_default_device_type_id)

    def _fire_station_id_domain(self):
        ids = [s.id for s in self.env.user.fire_station_ids]
        return [('id', 'in', ids)]

    @api.depends('location_id')
    def _compute_fire_station_id(self):
        for record in self:
            if record.location_id:
                return record.location_id.fire_station_id
            else:
                record.fire_station_id = request.session.fire_station_id or \
                       record.env['fire_station'].search(record._fire_station_id_domain(), limit=1)

    fire_station_id = fields.Many2one('fire_station', "Fire Station", domain=_fire_station_id_domain,
                                      compute=_compute_fire_station_id, inverse=lambda __: None)

    @api.constrains('date', 'device_id')
    def check_duplicate_inspection(self):
        date = fields.Datetime.from_string(self.date)
        date_start = fields.Datetime.to_string(date.replace(hour=0, minute=0, second=0))
        date_end = fields.Datetime.to_string(date.replace(hour=23, minute=59, second=59))
        domain = [
            ('device_id', '=', self.device_id.id),
            ('date', '>=', date_start),
            ('date', '<=', date_end),
            ('id', '!=', self.id)
        ]
        if self.env['inspection'].search_count(domain):
            raise ValidationError(_("Devices can be inspected only once a day."))

    @api.onchange('fire_station_id')
    def onchange_fire_station_id(self):
        if self.fire_station_id:
            ids = [l.id for l in self.fire_station_id.location_ids]
            location_domain = [('id', 'in', ids)]
        else:
            location_domain = []
        request.session.fire_station_id = self.fire_station_id.id
        if request.session.location_id and request.session.location_id in [l.id for l in self.fire_station_id.location_ids]:
            location_id = request.session.location_id
        else:
            location_id = self.env['location'].search(location_domain, limit=1)
        return {
            'domain': {'location_id': location_domain},
            'value': {
                'location_id': location_id,
                'fire_station_id': self.fire_station_id
            }
        }

    @api.onchange('location_id')
    def onchange_location_id(self):
        request.session.location_id = self.location_id.id
        ids = [d.id for d in self.location_id.device_ids]
        if self.device_type_id:
            ids = [i for i in ids if i in [d.id for d in self.device_type_id.device_ids]]
        return {
            'domain': {'device_id': [('id', 'in', ids)]},
            'value': {
                'device_id': False,
                'fire_station_id': self.location_id.fire_station_id
            }
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
