# -*- coding: utf-8 -*-{    'name': "Báo cáo/Tài liệu",    'summary': """        Tạo báo cáo, văn bản,cv liên quan đến thực tập sinh""",    'description': """        Long description of module's purpose    """,    'author': "KIDO",    'website': "http://www.yourcompany.com",    # Categories can be used to filter modules in modules listing    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml    # for the full list    'category': 'Uncategorized',    'version': '0.1',    # any module necessary for this one to work correctly    'depends': ['base','hh_intern'        # ,'website_form'                ],    # always loaded    'data': [        'security/ir.model.access.csv',        'security/security.xml',        # 'data/config_data.xml',        # 'views/document_web.xml',        'views/document_view.xml',        'views/document_menu.xml',    ],    # only loaded in demonstration mode    'demo': [        # 'demo/demo.xml',    ],    'application':  True,}