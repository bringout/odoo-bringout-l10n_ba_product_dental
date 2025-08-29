from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    def _get_dental_info(self):

        for line in self:
            ret = ''
            if line.product_id.product_tmpl_id.manufacturer_id:
                ret +=  '\nProizvođač: %s' % (line.product_id.product_tmpl_id.manufacturer_id.name)
            if line.product_id.product_tmpl_id.klasa:
                ret +=  '\nKlasa: %s' % (line.product_id.product_tmpl_id.klasa)
            if line.product_id.product_tmpl_id.keep_temp_from and line.product_id.product_tmpl_id.keep_temp_to:
                ret +=  '\nSkladištenje(°C): %d - %d' % (line.product_id.product_tmpl_id.keep_temp_from, line.product_id.product_tmpl_id.keep_temp_to)
            return ret
    
    def _get_sale_order_line_multiline_description_sale(self):
        """ We override this method because we decided that:
                The default description of a sales order line containing a ticket must be different than the default description when no ticket is present.
                So in that case we use the description computed from the ticket, instead of the description computed from the product.
                We need this override to be defined here in sales order line (and not in product) because here is the only place where the event_ticket_id is referenced.
        """
        #else:
        #    return super()._get_sale_order_line_multiline_description_sale()
        
        #return self._get_manufacturer_multiline_description() + self._get_sale_order_line_multiline_description_variants()

        return super()._get_sale_order_line_multiline_description_sale() \
               + self._get_dental_info()

