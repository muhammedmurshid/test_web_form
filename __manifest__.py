{
    'name': "Testing Web Module",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail',],
    'data': [
        'security/ir.model.access.csv',
        'views/back_form.xml',
        'views/web.xml',



    ],
    'demo': [],
    'summary': "testing_module",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}
