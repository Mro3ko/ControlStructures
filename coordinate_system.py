x=int(input("x="))
y=int(input("y="))
quadrant=""
if x>0:
    if y>0:
        quadrant="first"
    else:
        quadrant="fourth"
else:
    if y>0:
        quadrant="second"
    else:
        quadrant="third"

print(f"Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system")

