from odoo import api, fields, models


class Device(models.Model):
    _name = 'inspection911.device'
    _rec_name = 'rec_name'
    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    serial_number = fields.Char()
    description = fields.Char()
    location_ids = fields.Many2many('inspection911.location', 'location_device_rel', string="Locations")
    type_id = fields.Many2one('inspection911.device_type', string="Type", required=True, ondelete='cascade')
    brand_id = fields.Many2one('inspection911.brand', "Brand")
    make_id = fields.Many2one('inspection911.make', string="Make")
    inspection_ids = fields.One2many('inspection911.inspection', 'device_id', string="Inspections")

    @api.depends('inspection_ids.date')
    def _compute_last_inspection_date(self):
        inspections = self.env['inspection911.inspection']
        for record in self:
            last_inspections = inspections.search_read([('device_id', '=', record.id)], order='date desc', limit=1, fields=['date'])
            record.last_inspection_date = last_inspections and last_inspections[0]['date']

    last_inspection_date = fields.Datetime(compute=_compute_last_inspection_date, store=True)

    def _compute_rec_name(self):
        for record in self:
            values = [record.name, record.brand_id.name, record.make_id.name, record.description]
            values = [v for v in values if v]
            record.rec_name = ' - '.join(values)

    def _search_rec_name(self, operator, value):
        if operator == 'like':
            operator = 'ilike'
        domain = [
            '|', ('name', operator, value),
            '|', ('brand_id.name', operator, value),
            '|', ('make_id.name', operator, value),
            ('description', operator, value)
        ]
        return domain

    rec_name = fields.Char("Name", compute=_compute_rec_name, search=_search_rec_name)
