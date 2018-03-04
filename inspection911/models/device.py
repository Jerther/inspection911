from odoo import fields, models


class Device(models.Model):
    _name = 'device'
    _rec_name = 'rec_name'
    name = fields.Char(required=True)
    description = fields.Char()
    location_ids = fields.Many2many('location', 'location_device_rel', string="Locations")
    type_id = fields.Many2one('device_type', string="Type", required=True, ondelete='cascade')
    brand_id = fields.Many2one('brand', "Brand")
    make_id = fields.Many2one('make', string="Make")

    def _compute_rec_name(self):
        for record in self:
            record.rec_name = "%s %s %s" % (record.brand_id.name, record.make_id.name, self.name)

    rec_name = fields.Char(compute=_compute_rec_name)
