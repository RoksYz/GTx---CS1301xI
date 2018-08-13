principal = 5000
rate = 0.05
time = 5
goal = 7000

#Those three variables are given above again, as well as a
#fourth: goal. We want to see if the investment given by
#these values will exceed the goal. If it will, we want to
#print this message:
#  "You'll exceed your goal by [extra money]"
#If it will not, we want to print this message:
#  "You'll fall short of your goal by [needed money]"
#If the investor will meet their goal, [extra money] should
#be the final amount minus the goal. If the investor will
#not meet their goal, [needed money] will be the goal minus
#the final amount.
#
#To make the output more legible, though, we want to round
#the difference to two decimal places. If the difference is
#contained in a variable called 'difference', then we can
#do this to round it: rounded_diff = round(difference, 2)

import math

amount = principal * math.e **(rate * time)

extra= amount - goal
needed = goal - amount

rounded_extra = round(extra, 2)
rounded_needed = round(needed, 2)
if amount > goal:
    print("You'll exceed your goal by {}".format(rounded_extra))
else:
    print("You'll fall short of your goal by {}".format(rounded_needed))

