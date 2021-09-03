# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime, timedelta


class saleOrderArchive(models.Model):
    _name = 'sale_order_archive'

    name = fields.Char()
    order_create_date = fields.Date()
    customer = fields.Many2one('res.partner')
    sale_person = fields.Many2one('res.users')
    currency_id = fields.Many2one('res.currency')
    order_total_amount = fields.Monetary()
    count_of_lines = fields.Integer()

    def get_older_orders(self, older_than, state):
        return self.env['sale.order'].search([
            ('date_order', '<', datetime.now() - timedelta(older_than)), ('state', '=', state)])

    def convert_order_to_archive(self, order):
        return self.create({
            'name': order.name,
            'order_create_date': order.date_order,
            'order_total_amount': order.amount_total,
            'sale_person': order.user_id.id,
            'currency_id': order.currency_id.id,
            'customer': order.partner_id.id,
            'order_total_amount': order.amount_total,
            'count_of_lines': len(order.order_line),
        })


    def check_orders_to_archive(self):
        for order in self.get_older_orders(30, ('cancel', 'sale')):
            self.convert_order_to_archive(order)
            if order.state != 'cancel':
                order.state = 'cancel'
            order.unlink()
