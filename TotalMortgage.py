cost = 150000
rate = 0.0415
years = 15

rateMonths = rate/12
yearsMonths = years*12

result = cost*yearsMonths*rateMonths 
result01 = 1 -  ((1 + rateMonths) ** -yearsMonths)

resultFinal = result  / result01
final_cost = round(resultFinal,2)

print("The total cost of the house will be ${}".format(final_cost))