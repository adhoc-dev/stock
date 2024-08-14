##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models


class Stockpicking(models.Model):
    _inherit = 'stock.picking'

    def action_detailed_operations(self):
        action = super().action_detailed_operations()
        self.write({'return_lot_ids': self.move_line_ids.filtered(lambda l: l.qty_done > 0).mapped("lot_id")})
        return action
