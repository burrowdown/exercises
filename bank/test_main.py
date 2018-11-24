import unittest
import account
import bank
import main

class TestMain(unittest.TestCase):


    def setUp(self):
        self.test_account = account.Account("Ferdinand", 1, "cow", "5555")
        self.bank = bank.Bank()
        self.bank.user_store = {self.test_account.account_id: self.test_account}


    def test_logout(self):
        self.bank.active_user = self.test_account
        main.logout()
        self.assertEqual(self.bank.active_user, self.test_account)


if __name__ == '__main__':
    unittest.main()
