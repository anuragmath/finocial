# -*- coding: utf-8 -*-
{
    'name': "Core Lending",

    'summary': """
        Core Lending provides the basics of lending management""",

    'description': """
        Lending Core this module enables the abstract loan schedule generator and repayment and other principal 
        addons which are essentials for the core lending all other models will act as module associated to it
    """,

    'author': "Upscale Technologies",
    'website': "http://theupscale.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/loanaccount.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}