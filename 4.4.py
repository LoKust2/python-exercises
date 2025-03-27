largest = float('-inf')
hottest = 0
for i in range(1,13):
    num = input(f"Enter temperature of month {i}: ")
    n = float(num)
    if (n > largest):
        largest = n
        hottest = i

print(f"The month with the highest temperature is month {hottest}")