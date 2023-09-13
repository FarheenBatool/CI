price_sandwich = 100
price_chips = 50
price_coke = 70
x1 = 2  
x2 = 3  
x3 = 2  
budget = 500

total_cost = (x1 * price_sandwich + 
              x2 * price_chips + 
              x3 * price_coke)

remaining_budget = budget - total_cost
loss = budget - remaining_budget

print("Quantity of Sandwiches (x1):", x1)
print("Quantity of Chips (x2):", x2)
print("Quantity of Coke (x3):", x3)
print("Remaining Budget:", remaining_budget)
print("Loss:", loss)
