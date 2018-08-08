principal = 5000
rate = 0.05
time = 5

import math

amount = principal * math.e **(rate * time)

print("After " + str(time) + " years invested with a " + str(rate) + " interest rate, a $" + str(principal) + " investment will be worth $" + str(round(amount, 2)) + ".")

