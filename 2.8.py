import math

l = int(input("Length of rectangle: "))
w = int(input("Width of rectangle: "))

print(f"Area of rectangle: {l*w}")
print(f"Perimeter of rectangle: {2*l+2*w}")
print(f"Length of diagonal: {math.sqrt(pow(l,2) + pow(w,2)):.2f}")