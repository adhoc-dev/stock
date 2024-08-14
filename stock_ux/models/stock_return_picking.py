##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    reason = fields.Text('Reason for the return')

    def _create_returns(self):
        # add to new picking for return the reason for the return
        context = dict(self.env.context)
        new_picking, pick_type_id = super()._create_returns()
        picking = self.env['stock.picking'].browse(new_picking)
        picking = picking.with_context(context)
        picking.write({
            'note': self.reason,
            'return_picking_id': self.picking_id.id,
            'return_lot_ids': self.picking_id.return_lot_ids.ids,})
        if picking.return_lot_ids:
            # Agregar el campo return_lot_ids al contexto
            context['return_lot_ids'] = self.picking_id.return_lot_ids.ids     
        return new_picking, pick_type_id
