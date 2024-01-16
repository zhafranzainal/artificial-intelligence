print("Hello World")

print("""A 'Hello world!' program is generally a computer program that outputs or displays the message Hello World""")

# This is comment

"""
This is multiline comment
"""

movie_title = "Captain Marvel"
release_year = 2019
rating = 7.9
is_general_audiences = False

print("The movie is " + movie_title)

top_up_amount = 50
count = 3
discount = 2

total_payment = top_up_amount * count
total_discount = discount * count
payment_after_discount = total_payment - total_discount

print()
print("Total payment                    : RM " + str(total_payment))
print("Total payment (after discount)   : RM " + str(payment_after_discount))

print(
    """
    Burger Pricelist:
    1. Beef Burger RM15
    2. Cheese Burger RM20
    3. Kids Burger RM9
    """
)

menu_price = input("Menu price: ")
amount = input("Amount: ")
bill = int(menu_price) * int(amount)

print("You need to pay RM" + str(bill))

print()
firstName = input("Your first name  : ")
lastName = input("Your last name   : ")
classCode = input("Your class code  : ")

print("\nYour information:")
print(f"{firstName} {lastName}-{classCode}")
