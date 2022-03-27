import time

from get_exchange_rate import get_exchange_rate

# print("Enter a dollar amount in AUD...")
# print("then I'll convert it to PHP")

currency_from = input("What currency would you like to convert from: e.g. AUD, PHP etc.")
currency_to = input("What current would you like to convert to?")

user_input = input("Enter you dollar amount:")

print(f"You input {user_input}")

time.sleep(1)

# pull this number from an api
conversion = get_exchange_rate(currency_from, currency_to)

users_new_dollar_value = round(float(user_input) * conversion, 2)

print(f"That is {users_new_dollar_value} {currency_to}.")
