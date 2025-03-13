import math

fuel_tank = int(input("Enter gallons in tank: "))
gas_price = float(input("Enter gas price: "))
efficiency = int(input("Enter efficiency (MPG): "))

cost_100 = (100/efficiency)*gas_price
total_dist = fuel_tank*efficiency

print(f"Cost per 100 miles: {cost_100:.2f}")
print(f"Total distance possible: {total_dist:.2f}")