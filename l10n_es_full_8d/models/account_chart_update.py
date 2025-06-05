from odoo import _, models
from odoo.addons.account.models.chart_template import template

class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('es_coop_full')
    def _get_es_coop_full_template_data(self):
        return {
            'name': _('Cooperatives - Complete (2008)'),
            'parent': 'es_coop_pymes',
            'code_digits': 8,
        }

    @template('es_coop_pymes')
    def _get_es_coop_pymes_template_data(self):
        return {
            'name': _('Cooperatives - SMEs (2008)'),
            'parent': 'es_common',
        }
