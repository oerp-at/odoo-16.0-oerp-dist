
{
    'name': "first_try",

    'summary': "Create view and access rights for user",
    'author': "First Try",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [ 'views/first_try_views.xml',
              'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [        
    ],
}
