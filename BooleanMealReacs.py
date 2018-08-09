hot = True
cold = False
morning = True
evening = False
night = False


Soup = False
Biscuit= False
Cereal= True
Pizza= False

if cold and evening or night == True:
    Soup = True
else:
    Soup = False
if morning and cold == True:
    Biscuit = True
else:
    Biscuit = False
if morning and hot or  night == True:
    Cereal = True
else:
    Cereal = False
if evening or night == True:
    Pizza = True
else:
    Pizza = False

print("Soup: {}".format(Soup))
print("Biscuit: {}".format(Biscuit))
print("Cereal: {}".format(Cereal))
print("Pizza: {}".format(Pizza))