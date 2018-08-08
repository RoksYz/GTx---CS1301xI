meal_cost = 10.00
tax_rate = 0.08
tip_rate = 0.20

tax = tax_rate*meal_cost
tip = tip_rate*meal_cost
total = meal_cost+tax+tip

print("Subtotal: {}".format(meal_cost))
print("Tax: {}".format(tax))
print("Tip: {}".format(tip))
print("Total: {}".format(total))