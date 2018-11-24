def get_user_int(message):
    while True:
        try:
            number_in = input(message)
            number_in_clean = number_in.replace(",", "").replace("$", "")
            dollars, point, cents = number_in_clean.partition(".")
            dollars = int(dollars)
            if cents:
                    print("\n******** This bank only deals in whole dollars. Keep your $0." + cents)
            while dollars < 0:
                print("Please enter a positive number")
                dollars = int(input(message))
            return dollars
        except ValueError:
            print("Please enter a whole number.")
