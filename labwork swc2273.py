def convert_currency():
    print("Currency Conversion Program\n")
    print("Exchange Rates:")
    print("USD - US Dollar     : 0.25")
    print("EUR - Euro          : 0.21")
    print("GBP - British Pound : 0.18\n")
    print("Choose The Target Currency:")
    print("1. USD - US Dollar")
    print("2. EUR - Euro")
    print("3. GBP - British Pound\n")

    choice = input("Enter your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter a number from the menu.")
        choice = input("Enter your choice (1-3): ")
    print("")

    amount_myr = float(input("Enter the amount in Malaysia Ringgit (MYR): "))
    target_currency = ['USD', 'EUR', 'GBP'][int(choice) - 1]

    exchange_rates = {'USD': 0.25, 'EUR': 0.21, 'GBP': 0.18}
    converted_amount = amount_myr * exchange_rates[target_currency]

    print("")
    print(f"Equivalent amount in {target_currency}: {converted_amount:.2f}")
convert_currency()
