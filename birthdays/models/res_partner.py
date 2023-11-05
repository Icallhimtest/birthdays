# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date('Date of Birth')

    @api.model
    def _cron_birthday_wishes(self):
        template = self.env.ref('birthdays.birthday_wishes')
        for partner in self.search([('birthday', '=', fields.Date.today())]):
            template.send_mail(partner.id)
