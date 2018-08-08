amount = 67

quarters, amount = divmod(amount, 25)
dimes, amount = divmod(amount, 10)
nickels, pennies = divmod(amount, 5)


print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)