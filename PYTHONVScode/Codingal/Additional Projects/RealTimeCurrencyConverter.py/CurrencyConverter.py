from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter you amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

# print(F"from {from_currency} to {to_currency}, Converted Amount: {c.convert(from_currency,to_currency,amount)}")

# try:
#     converted_amount = c.convert(from_currency, to_currency, amount)
#     print(f"From {from_currency} to {to_currency}, Converted Amount: {converted_amount}")
# except ValueError:
#     print("Invalid currency code or amount provided.")
# except forex_python.converter.RatesNotAvailableError:
#     print("Currency conversion rates are not available.")