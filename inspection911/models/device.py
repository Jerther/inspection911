from odoo import fields, models


class Device(models.Model):
    _name = 'device'
    _rec_name = 'rec_name'
    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    serial_number = fields.Char()
    description = fields.Char()
    location_ids = fields.Many2many('location', 'location_device_rel', string="Locations")
    type_id = fields.Many2one('device_type', string="Type", required=True, ondelete='cascade')
    brand_id = fields.Many2one('brand', "Brand")
    make_id = fields.Many2one('make', string="Make")

    def _compute_last_inspection_date(self):
        for record in self:
            record.last_inspection_date = fields.Datetime.now()

    last_inspection_date = fields.Datetime(compute=_compute_last_inspection_date)

    def _compute_rec_name(self):
        for record in self:
            record.rec_name = "%s - %s - %s - %s" % (record.name, record.brand_id.name, record.make_id.name, record.description or '')

    rec_name = fields.Char(compute=_compute_rec_name)
