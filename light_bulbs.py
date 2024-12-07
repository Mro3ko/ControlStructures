#A lamp in a room has three light bulbs.
# Switch one lights one bulb, and switch two lights the other two bulbs.
# Write a program that tells you how many bulbs are lit, depending on the state of switch one and switch two.

ligh_switch1=False
ligh_switch2=False
bulbs_on=0

if ligh_switch1:
    bulbs_on+=1
if ligh_switch2:
    bulbs_on+=2
print(f"{bulbs_on} light bulbs are on")