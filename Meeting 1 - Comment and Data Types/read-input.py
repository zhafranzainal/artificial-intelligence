print(
    """
    Burger Pricelist:
    1. Beef Burger RM15
    2. Cheese Burger RM20
    3. Kids Burger RM9
    """
)

menu_price = input("Menu price   : ")
amount = input("Amount       : ")

bill = int(menu_price) * int(amount)

print("\nYou need to pay RM" + str(bill))
