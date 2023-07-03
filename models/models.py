# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random

COLORS = ['#F06050', '#F4A460', '#F7CD1F', '#6CC1ED', '#e776b5', '#f1a908',
          '#EB7E7F', '#2C8397', '#80d7a3', '#D6145F', '#30C381', '#9365B8']

class StockWarehouse(models.Model):
    _inherit ="stock.warehouse"

    nb_article = fields.Float("Nombre d'article", compute="_compute_nb_article")
    sales_value = fields.Float("Valeur de vente", compute="_compute_sales_value")
    purchases_value = fields.Float("Valeur d'achat", compute="_compute_purchases_value")
    bg_color = fields.Char(string="Couleur", compute="get_kanban_color")

    def get_kanban_color(self):
        for rec in self:
            if not rec.bg_color:
                rec.bg_color = rec.get_random_color()

    def get_random_color(self):
        color = random.choice(COLORS)
        picked_colors = []
        if not self.search([]).filtered(lambda s: s.bg_color == color):
            return color
        else:
            picked_colors.append(color)
            # Check if all available colors are taken, then pick this color
            if set(picked_colors) == set(COLORS):
                return color
            else:
                self.get_random_color()

    def _compute_nb_article(self):
    	for rec in self:
    		stock_quant_ids = self.env['stock.quant'].sudo().search([('location_id', '=', rec.lot_stock_id.id)])
    		quantity = sum(stock_quant_ids.mapped('quantity')) - sum(stock_quant_ids.mapped('reserved_quantity'))
    		rec.nb_article = quantity

    def _compute_sales_value(self):
    	for rec in self:
    		sale_order_ids = self.env['sale.order'].sudo().search([('state', 'in', ['sent', 'sale', 'done']), ('warehouse_id', '=', rec.id)])
    		rec.sales_value = sum(sale_order_ids.mapped('amount_total'))

    def _compute_purchases_value(self):
    	for rec in self:
    		picking_type_ids = self.env['stock.picking.type'].sudo().search([('warehouse_id', '=', rec.id)])
    		purchase_order_ids = self.env['purchase.order'].sudo().search([('picking_type_id', 'in', picking_type_ids.ids)])
    		rec.purchases_value = sum(purchase_order_ids.mapped('amount_total'))