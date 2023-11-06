# -*- coding: utf-8 -*-
from odoo import fields
from odoo.tests.common import TransactionCase

# import logging
# _logger = logging.getLogger(__name__)


class TestBirthdaysCommon(TransactionCase):

    # -------------------------------------------------------------------------
    # DATA GENERATION
    # -------------------------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        super(TestBirthdaysCommon, cls).setUpClass()
        cls.partner = cls.env['res.partner'].create({
            'name': 'Birthday man',
            'birthday': fields.Date.today(),
        })
