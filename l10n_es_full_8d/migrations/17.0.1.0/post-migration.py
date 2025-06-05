from odoo import api, SUPERUSER_ID
from odoo.tools import sql
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})

    _logger.info('Starting account code migration')

    # Obtener todas las compañías que usan el plan contable español
    companies = env['res.company'].search([
        ('chart_template', 'in', ['es_full', 'es_pymes', 'es_coop_full', 'es_coop_pymes'])
    ])

    _logger.info('Found %d companies to update', len(companies))

    if not companies:
        return

    # Actualizar cuentas usando SQL directo para mejor rendimiento
    query = """
        UPDATE account_account
        SET code = CONCAT(
            SUBSTRING(code, 1, 3),
            '00',
            SUBSTRING(code, 4, 3)
        )
        WHERE LENGTH(code) = 6
        AND company_id IN %s
        AND code ~ '^[0-9]+$'
    """
    cr.execute(query, [tuple(companies.ids)])

    # Actualizar secuencias relacionadas
    env['account.account']._adapt_accounts_for_account_groups(companies.ids)

    _logger.info('Migration completed')
