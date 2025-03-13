import math
print("Enter radius: ", end='')
r = int(input())
pi = 3.1416
area_2d = pi*pow(r,2)
circum_2d = 2*pi*r
volume_3d = 4/3*pi*pow(r,3)
area_3d = 4*pi*pow(r,2)

print(f"Circle Area: {area_2d:.2f}\nCircumference: {circum_2d:.2f}\nSphere Volume: {volume_3d:.2f}\nSphere Surface Area: {area_3d:.2f}")