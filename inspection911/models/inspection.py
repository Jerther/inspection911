from odoo import fields, models


class Inspection(models.Model):
  _name = 'inspection'
  fire_station_id = fields.Many2one('fire_station', "Fire Station", required=True)
  device_id = fields.Many2one('device', "Device", required=True)
  fireman_id = fields.Many2one('fireman', "Fireman", required=True)
  complies = fields.Boolean()
  comment = fields.Html()
  date = fields.Datetime(required=True, default=fields.Datetime.now())
