import account
import bank
import utils


print("\n\n~~~ Welcome to AltSource Bank ~~~")
bank = bank.Bank()


def authorize():
    if bank.active_user == None:
        print("You are not logged in")
        return False
    else:
        return True


def logout():
    if authorize():
        bank.active_user = None
        print("Successfully logged out")


def check_status():
    try:
        bank.active_user.check_status()
    except AttributeError:
        authorize()


def deposit():
    if authorize():
        amount = utils.get_user_int("Amount to deposit: $")
        bank.active_user.deposit(amount)


def withdraw():
    if authorize():
        amount = utils.get_user_int("Amount to withdraw: $")
        bank.active_user.withdraw(amount)


def history():
    if authorize():
        print("\n\nDATE \t TRANSACTION \t BALANCE")
        for entry in bank.active_user.history:
            print(entry)


def menu():
    return input(
        "\n\n_____________________________________________\n\n"
        "Please choose from the following menu options: \n\n"
        "> Press 1 to create an account \n"
        "> Press 2 to log in \n"
        "> Press 3 to log out \n"
        "> Press 4 to check your account status \n"
        "> Press 5 to make a deposit \n"
        "> Press 6 to make a withdrawal \n"
        "> Press 7 to view account history \n"
        "> Press 0 to quit"
        "\n\n_____________________________________________\n\n::"
    )

actions = {
    "1": bank.create_account,
    "2": bank.login,
    "3": logout,
    "4": check_status,
    "5": deposit,
    "6": withdraw,
    "7": history,
    "0": exit
}


if __name__ == '__main__':
    action = False
    while action != "9":
        try:
            actions[menu()]()
        except KeyError:
            print("That is not a valid command")
            menu()



    # TODO:
    # dollar signs everywhere
    # allow $ and , and .
    # change ints to floats???
    # clean up whitespace
    # clean up " vs "
    # uniqueness constraint on account numbers
    # TESTS
    # can the UI be the same in every command?
    # Comment everything
    # quit at any point?
