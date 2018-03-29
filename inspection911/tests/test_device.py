from odoo import tests


class TestDevice(tests.TransactionCase):
    def setUp(self):
        super().setUp()
        brand = self.env['inspection911.brand'].create({'name': "a brand"})
        make = self.env['inspection911.make'].create({'name': "a make", 'brand_id': brand.id})
        type = self.env['inspection911.device_type'].create({'name': "a type"})
        self._device = self.env['inspection911.device'].create({'name': "a device", 'make_id': make.id, 'type_id': type.id})
        station = self.env['inspection911.fire_station'].create({'name': "a device"})
        self._location = self.env['inspection911.location'].create({'name': "a location", 'fire_station_id': station.id})

    def test_last_inspection_date(self):
        vals = {
            'location_id': self._location.id,
            'device_id': self._device.id,
            'date': '2000-01-01 00:00:00'
        }
        self.env['inspection911.inspection'].create(vals)
        vals['date'] = '2000-01-02 00:00:00'
        self.env['inspection911.inspection'].create(vals)
        vals['date'] = '1999-12-01 23:59:59'
        self.env['inspection911.inspection'].create(vals)
        self.assertEqual('2000-01-02 00:00:00', self._device.last_inspection_date)
