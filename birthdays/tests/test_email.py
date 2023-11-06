# -*- coding: utf-8 -*-
from odoo.tests import tagged
from odoo.addons.birthdays.tests.common import TestBirthdaysCommon

import logging
_logger = logging.getLogger(__name__)


@tagged('birthdays', 'at_install')
class TestBirthdayEmail(TestBirthdaysCommon):

    # -------------------------------------------------------------------------
    # TESTS: Animal Hunger
    # -------------------------------------------------------------------------

    def test_email(self):
        self.env['res.partner']._cron_birthday_wishes()
        birthday_message = self.env['mail.message'].search(
            [('model', '=', 'res.partner'),
             ('res_id', '=', 41)], order='id desc', limit=1)
        self.assertIn("happy birthday", birthday_message.body)
