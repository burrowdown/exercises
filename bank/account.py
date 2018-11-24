from datetime import datetime


class Account:

    def __init__(self, owner, balance, animal, account_id):
        self.owner = owner
        self.balance = balance
        self.animal = animal
        self.account_id = account_id
        self.history = [self._write_history(self.balance, "initial deposit")]


    def check_status(self):
        print(
            "\n======================================\n"
            "You are logged in as {0}\n"
            "Account number: {1}\n"
            "Current balance: ${2}\n"
            "======================================"
            .format(self.owner, self.account_id, self.balance))
        return self


    def deposit(self, amount):
        # Perform deposit
        self._change_balance("deposit", amount)
        self.check_status()
        return self


    def withdraw(self, amount):
        if self.balance <= 0:
            print("You have no balance to withdraw")
            return self
        # Perform withdrawal
        self._change_balance("withdraw", amount)
        self.check_status()
        return self


    def _change_balance(self, message, amount):
        '''Get amount from user'''
        if message == "withdraw":
            if amount > self.balance:
                print("You don't have {} to withdraw. Your current balance is ${}".format(amount, str(self.balance)))
                return amount
            amount = 0 - amount
            message = "withdrawal"

        self.balance += amount

        print("\n${0} {1} successful".format(abs(amount), message).upper())
        self.history.append(self._write_history(amount, message))

        return amount


    def _write_history(self, amount, message):
        now = datetime.now()
        time_string = now.strftime("%Y %b %m, %H:%M" )
        entry = "{0} \t{1}: ${2} \tbalance: ${3}".format(time_string, message, str(abs(amount)), self.balance)
        return entry
