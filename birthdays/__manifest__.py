# -*- coding: utf-8 -*-
{
    'name': "birthdays",

    'summary': """
        Send partner birthday wishes""",

    'description': """
        Send partner birthday wishes
    """,

    'author': "dve@odoo.com",
    'website': "www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/crons.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
