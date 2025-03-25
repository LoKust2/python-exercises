import numpy as np

# a) The sum of all numbers between 2 and 100
print("a) The sum of all numbers between 2 and 100")
k = 0
for i in range(2, 102, 2):
    k += i
    

print (k)

# b) The sum of all squares between 1 and 100
print("\nb) The sum of all squares between 1 and 100")
j = 1
m = 0
p= 0
while (m <= 100):
    m = j*j
    p = p + m
    j += 1

print(p)

# c) All powers of 2 from 0 to 20
print("\nc) All powers of 2 from 0 to 20")
i = 0
for i in range (21):
    p = np.power(2,i)
    print (f"2^{i}: {p}")

# d) Sum of all odd numbers between a and b, where a and b are inputs
print("\nd) Sum of all odd numbers between a and b, where a and b are inputs")
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
k = 0
if (a%2 == 0):
    for i in range(a+1, b+1, 2):
        k += i
else:
    for i in range(a, b+1, 2):
        k += i

print (k)

# e) Sum of all odd digits of an input number
print("\ne) Sum of all odd digits of an input number")

num = input("Enter a number: ")

digits = list(num)
sum = 0
for i in digits:
    if (int(i)%2 == 1):
        sum += int(i)

print(sum)