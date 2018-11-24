import unittest
import account

class TestAccount(unittest.TestCase):


    def setUp(self):
        self.test_account = account.Account("Ferdinand", 1, "cow", "5555")


    def test_account_creation(self):
        self.assertTrue(isinstance(self.test_account, account.Account))


    def test_account_attributes(self):
        self.assertEqual(self.test_account.owner, "Ferdinand")
        self.assertEqual(self.test_account.balance, 1)
        self.assertEqual(self.test_account.animal, "cow")
        self.assertEqual(self.test_account.account_id, "5555")
        self.assertEqual(len(self.test_account.history), 1)


    def test_deposit(self):
        self.test_account.deposit(1)
        self.assertEqual(self.test_account.balance, 2)


    def test_withdraw(self):
        self.test_account.withdraw(1)
        self.assertEqual(self.test_account.balance, 0)


    def test_history(self):
        self.test_account.deposit(1)
        self.assertEqual(len(self.test_account.history), 2)
        self.test_account.withdraw(1)
        self.assertEqual(len(self.test_account.history), 3)


if __name__ == '__main__':
    unittest.main()
