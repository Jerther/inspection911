from odoo import fields, models


class Device(models.Model):
    _name = 'device'
    uid = fields.Char(required=True)
    description = fields.Char()
    location_ids = fields.Many2many('location', 'location_device_rel', string="Locations")
    type_id = fields.Many2one('device_type', string="Type", required=True, ondelete='cascade')
    make_id = fields.Many2one('make', string="Make", required=True, ondelete='cascade')
