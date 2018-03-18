{
    'name': "Inspection 911",

    'summary': """
        Equipment inspections for fire stations.""",

    'description': """
        Periodical inspection of all equipments in a fire station.
    """,

    'author': "Jerther",
    'website': "http://github.com/Jerther/inspection911",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        'data/groups.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/make.xml',
        'views/brand.xml',
        'views/device.xml',
        'views/device_type.xml',
        'views/fire_station.xml',
        'views/location.xml',
        'views/res_users.xml',
        'views/inspection.xml',
    ],
}