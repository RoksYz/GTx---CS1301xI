STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60


Modifier = STAB*Type*Critical*Other*(Random)
damage01 = ((2*Level+10)/250)
damage02 = damage01*Attack/Defense
damage = (damage02*Base+2)*Modifier

print(damage)
