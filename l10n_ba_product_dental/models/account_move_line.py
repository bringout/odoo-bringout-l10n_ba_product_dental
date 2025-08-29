from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.depends('product_id', 'move_id.payment_reference')
    def _compute_name(self):

        def get_name(line):
            values = []
            if line.partner_id.lang:
                product = line.product_id.with_context(lang=line.partner_id.lang)
            else:
                product = line.product_id

            if product.partner_ref:
                values.append(product.partner_ref)
            if line.journal_id.type == 'sale':
                if product.description_sale:
                    values.append(product.description_sale)
            elif line.journal_id.type == 'purchase':
                if product.description_purchase:
                    values.append(product.description_purchase)
            return '\n'.join(values)

  
        super(AccountMoveLine, self)._compute_name()

        for line in self:
            if not line.product_id or line.display_type in ('line_section', 'line_note', 'payment_term'):
                continue

            if line.product_id.manufacturer_id:
                line.name +=  '\nProizvođač: %s' % (line.product_id.manufacturer_id.name)
            if line.product_id.klasa:
                line.name +=  '\nKlasa: %s' % (line.product_id.manufacturer_id.name)
            if line.product_id.keep_temp_to and line.product_id.keep_temp_to:
                line.name +=  '\nSkladištenje(°C): %d - %d' % (line.product_id.manufacturer_id.name)
