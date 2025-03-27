# Write a program that reads a set of floating-point values. Ask the user to enter the values, then print:
sum = 0
count = 0
smallest = float('inf')
largest = float('-inf')

while (1):
    num = input("Enter float or // to exit: ")
    if (num == '//'):
        break
    else:
        n = float(num)
        sum += n
        count += 1

        if (n < smallest):
            smallest = n
        if (n > largest):
            largest = n

range = largest - smallest
print(f"The average of the numbers: {sum/count:.3f}")
print(f"The smallest number: {smallest}")
print(f"The largest number: {largest}")
print(f"The range of the numbers: {range}")