top_up_amount = 50
count = 3
discount = 2

total_payment = top_up_amount * count
total_discount = discount * count
payment_after_discount = total_payment - total_discount

print()
print("Total payment                    : RM " + str(total_payment))
print("Total payment (after discount)   : RM " + str(payment_after_discount))
