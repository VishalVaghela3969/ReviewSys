# -*- coding: utf-8 -*-
{
    'name': "RateMyBizz",

    'author': "Vishal Vaghela",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '16.0.0.0.1',

    'depends': ['base','website'],

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
        'views/interaction.xml',
        'views/user_sign_in_website.xml',
        'report/business_report.xml',
        'report/xlsx_business_report.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
