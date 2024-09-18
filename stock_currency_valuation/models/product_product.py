from odoo import models, fields


class productProduct(models.Model):

    _inherit = 'product.product'

    valuation_currency_id = fields.Many2one(
        related="categ_id.valuation_currency_id",
        currency_field='valuation_currency_id'
    )
    standard_price_in_currency = fields.Float(
        'Cost in currency', company_dependent=True,
        groups="base.group_user",
    )
