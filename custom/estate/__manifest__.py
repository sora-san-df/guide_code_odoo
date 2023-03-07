{
    'name': "State module",
    'version': '1.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,

    
     # add the property 'application' so my module can be considered a full app in odoo
    'application': True,
    'installable': True,

    # data files always loaded at installation
    'data': [
        
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        
    ],

}