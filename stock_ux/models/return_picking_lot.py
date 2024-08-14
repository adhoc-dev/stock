# Copyright 2022 Open Source Integrators (https://www.opensourceintegrators.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, exceptions, models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    return_picking_id = fields.Many2one(
        comodel_name="stock.picking", store=True
    )
    return_lot_ids = fields.Many2many("stock.lot", string="lotes de la entrega devuelta", copy=False, store = True)

    def button_validate(self):
        res = super().button_validate()
        if not self.return_picking_id and self.picking_type_id.code == 'outgoing':
            self.write({'return_lot_ids': self.move_line_ids.filtered(lambda l: l.qty_done > 0).mapped("lot_id")})
        if self.return_picking_id:
            for rec in self.move_line_ids:
                if self.return_lot_ids:
                    if rec.lot_id and rec.product_id.tracking == 'serial':
                        self.return_picking_id.write({
                            'return_lot_ids': [(3, rec.lot_id.id)]
                        })
                    if rec.lot_id and rec.product_id.tracking == 'lot':
                        if rec.reserved_uom_qty == sum(self.return_picking_id.sale_id.order_line.filtered(lambda l: l.product_id == rec.product_id).mapped('qty_delivered')):
                            self.return_picking_id.write({
                                'return_lot_ids': [(3, rec.lot_id.id)]
                            })

        return res
