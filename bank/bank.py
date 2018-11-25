from account import Account
from random import randint


class Bank:


    def __init__(self):
        self.user_store = dict()
        self.active_user = None


    def create_account(self):
        # Get user input
        owner = input("What is the account holder's name?    ")
        animal = input("What is your favorite animal?    ").lower()
        starting_balance = self.get_user_int("What is the initial deposit?   $")
        account_number = str(randint(1000, 9999))
        print("\n======================================\n"
              "Account successfully created for {0}\n"
              "Current balance is ${1}\n"
              "Your account number is: {2}\n"
              "You will need this number for future transactions.\n"
              "======================================"
              .format(owner, starting_balance, account_number))

        # Create new account, add to user store, and log in
        new_account = Account(owner, starting_balance, animal, account_number)
        self.user_store[new_account.account_id] = new_account
        self.active_user = new_account

        return new_account


    def remove_account(self):
        print("\n\nHere is your balance of ${}. "
              "Your account is hereby closed."
              .format(self.active_user.balance))
        self.user_store.pop(self.active_user.account_id, None)
        self.active_user = None


    def login(self):
        if self.active_user != None:
            print("You are already logged in. To switch accounts, log out first.")
            return self.active_user

        # Get account instance from account number
        account_number = self._get_valid_account_number()
        account = self.user_store[account_number]

        # Validate user passphrase
        if self._validate_animal(account):
            # Perform login
            self.active_user = account
            print("Welcome, {0}. Your current balance is {1}."
                  .format(account.owner, account.balance))
            return account


    def get_user_int(self, message):
        while True:
            try:
                number_in = input(message)
                # Strip out ',' and '$', split by '.' and discard what follows
                number_in_clean = number_in.replace(",", "").replace("$", "")
                dollars, point, cents = number_in_clean.partition(".")
                dollars = int(dollars)
                if cents:
                        print("\nThis bank only deals in whole dollars."
                              "Keep your $0." + cents)
                if dollars >= 0:
                    return dollars
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a whole number.")


    def _get_valid_account_number(self):
        account_number = input("Account number: ")
        while account_number not in self.user_store:
            if account_number == "x":
                return None
            else:
                account_number = input(
                    "\nThat is not a valid account number. "
                    "Try again, or type 'x' to return to the main menu. "
                    "\n\nAccount number: "
                )
        return account_number


    def _validate_animal(self, account):
        while True:
            passphrase = input("What is your favorite animal?").lower()
            if passphrase == account.animal:
                return True
            else:
                print("That's not what you told me last time.")
