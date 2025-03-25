import numpy as np

# Write programs that read a sequence of integer inputs and print:

largest = float('-inf')
smallest = float('inf')

odd = 0
even = 0

total = 0
totals = list()

storage = list()
dupes = set()
while (1):
    num = input("Enter an integer or // to exit: ")
    if (num == '//'):
        break
    else:
    # a) The smallest and largest of the inputs.
        n = int(num)

        if (n > largest):
            largest = n
        if (n < smallest):
            smallest = n

    # b) The number of even and odd inputs.
        if (n%2 == 0):
            even += 1
        else:
            odd += 1

    # c) Cumulative totals.
        total += n
        totals.append(total)

    # d) All adjacent duplicates.
        storage.append(n)

print("a) The smallest and largest of the inputs:")
print(f"{smallest}, {largest}\n")

print("b) The number of even and odd inputs:")
print(f"{even}, {odd}\n")

print("c) Cumulative totals:")
for total in totals:
    print(total, end = ' ')

tmp = float('-inf')
for i in storage:
    if i == tmp:
        dupes.add(i)
    tmp = i
    
print("\nd) All adjacent duplicates:")
for dupe in dupes:
    print(dupe, end = ' ')