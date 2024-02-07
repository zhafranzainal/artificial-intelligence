# Function definition

def order_pizza():
    quantity = 7
    price = 10
    total_order = quantity * price

    print(f"Total order is ${total_order}")


def order_pizza_dynamic(quantity):
    price = 10
    total_order = quantity * price

    print(f"Total order is ${total_order}")


# Function calling
order_pizza()
order_pizza_dynamic(7)
