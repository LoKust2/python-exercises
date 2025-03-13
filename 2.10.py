import math

car_cost = int(input("Enter cost of car: "))
distance = int(input("Enter miles per year: "))
gas_price = int(input("Enter gas price: "))
efficiency = int(input("Enter efficiency (MPG): "))
resale_value = int(input("Enter resale price: "))    

gas_cost = (distance*5/efficiency)*gas_price

print(f"Total cost of ownership: {car_cost + gas_cost - resale_value:.2f}")