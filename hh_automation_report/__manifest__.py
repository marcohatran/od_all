# -*- coding: utf-8 -*-
{
    'name': "Gui bao cao tu dong",

    'summary': """
        Gui bao cao tu dong""",

    'description': """
        Gui bao cao tu dong
    """,

    'author': "KIDO",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hh_intern','report_xlsx','hh_intern_pass_report'
                # 'hh_report'
                ],


    # always loaded
    'data': [
        'views/cron_view.xml',
        'views/report_view.xml',
        'views/report_menu.xml',
        'views/template.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [

    ],

    'application':  True,
}