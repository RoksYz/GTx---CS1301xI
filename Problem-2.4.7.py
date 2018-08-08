dosage = 100
time_since_last_dose = 7
is_nighttime = False
took_something_cross_reactive = False

if took_something_cross_reactive == False:
    if is_nighttime == True:
        time_since_last_dose*=2
        dosage = time_since_last_dose*dosage
    else:
        dosage = time_since_last_dose*dosage
else:
    dosage = 0
    
print(dosage)