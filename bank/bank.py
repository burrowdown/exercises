from account import Account
from random import randint
import utils


class Bank:

    def __init__(self):
        self.user_store = dict()
        self.active_user = None

    def create_account(self):
        owner = input("What is the account holder's name?    ")
        animal = input("What is your favorite animal?    ").lower()
        starting_balance = utils.get_user_int("What is the initial deposit?    $")
        account_number = str(randint(1000, 9999))
        # TODO: think more about the UX here, combine with check_status?
        print(
            "\n======================================\n"
            "Account successfully created for {0}\n"
            "Current balance is ${1}\n"
            "Your account number is: {2}\n"
            "You will need this number for future transactions.\n"
            "======================================"
            .format(owner, starting_balance, account_number))

        new_account = Account(owner, starting_balance, animal, account_number)
        self.user_store[new_account.account_id] = new_account
        self.active_user = new_account

        return new_account


    def remove_account(self, account):
        # comment here
        self.user_store.pop(account, None)
        self.active_user = None


    def login(self):

        if self.active_user != None:
            print("You are already logged in. To switch accounts, log out first.")
            return self.active_user

        account_number = self._get_valid_account_number()

        # Get account instace from account number
        account = self.user_store[account_number]

        if self._validate_animal(account):
            # Login complete
            self.active_user = account
            print("Welcome, {0}. Your current balance is {1}.".format(account.owner, account.balance))
            return account


    def _get_valid_account_number(self):
        account_number = input("Account number: ")
        while account_number not in self.user_store:
            if account_number == "x":
                return None
            else:
                account_number = input("That is not a valid account number. Try again, or type 'x' to return to the main menu. \n\nAccount number: ")
        return account_number

    def _validate_animal(self, account):
        while True:
            passphrase = input("What is your favorite animal?").lower()
            if passphrase == account.animal:
                return True
            else:
                print("That's not what you told me last time.")
