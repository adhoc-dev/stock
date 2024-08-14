from odoo import models, fields, api


class StockProductionLot(models.Model):
    _inherit = 'stock.lot'

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        domain = domain or []
        return_lot_ids = self._context.get('return_lot_ids', False)
        # import pdb;pdb.set_trace()
        if return_lot_ids and isinstance(return_lot_ids, list):
            domain.append(('id', 'in', return_lot_ids))
        # import pdb;pdb.set_trace()
        return super()._name_search(name, domain, operator, limit, order)
