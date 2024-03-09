# -*- coding: utf-8 -*-
{
    'name': "demo_1",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_seq.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/business.xml',
        'views/user.xml',
        'views/review.xml',
        'views/category.xml',
        'views/product.xml',
        'views/image.xml',
        'views/tags.xml',
        'views/business_tags.xml',
        'views/review_comments.xml',
        'views/business_owner.xml',
        'views/user_favourite.xml',
    ]
}
