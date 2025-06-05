{
    'name': 'Spanish Localization - Cooperatives (8 digits)',
    'version': '17.0.1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Spanish charts of accounts (PGCE 2008) - Cooperatives (8 digits)
===============================================================
    """,
    'depends': ['account', 'l10n_es'],
    'data': [
    ],
    'post_init_hook': '_post_init_migrate',
    'license': 'LGPL-3',
}
