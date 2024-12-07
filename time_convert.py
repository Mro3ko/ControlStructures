time=input("Enter time (24-hour format): ")
h=int(time[0:2])
m=int(time[-2:])
h=h%12
print(f"Time in 12-hour format: {h}:{m}pm")