
from odoo import SUPERUSER_ID, Command
from odoo.exceptions import RedirectWarning, UserError, ValidationError
from odoo.tests.common import  TransactionCase, tagged
from odoo.tools import mute_logger
from odoo.tools.safe_eval import safe_eval, const_eval, expr_eval



class FirstTryTest(TransactionCase):
    """ A few tests for a 'Standard' (i.e. PostgreSQL) sequence. """

    def test_all_kinds(self):
        model = self.env['first_try.key_value']
        create_record = model.create([{'name':'test123test','value':'123'},
                                      {'name':'test567test','value':'1234567'},
                                      {'name':'test89test','value':'123456789'}])
        print (create_record,'#'*23)


        self.assertEqual(len(create_record), 3,
                              "3 records should have been created ")
        search_test_records = model.search([('name','like', 'test___test')])
        self.assertEqual(len(search_test_records.ids), 2,
                              "2 records should have 3 chars between test")
        create_record.unlink()
        search_test_records = model.search([('name', 'like', 'test%test')])
        self.assertEqual(len(search_test_records.ids), 0,
                              "no test records should exist")