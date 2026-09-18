""" Exercise 1 """

points = 50
points_gained = 10
points_lost = 5
final_score = points + points_gained - points_lost
print(final_score)

""" Exercise 2 """

recipe_serves = 4
num_eggs = 2
cheese_ounces = 4
num_guests = 6

eggs_needed = (num_eggs / recipe_serves) * num_guests
cheese_needed = (cheese_ounces / recipe_serves) * num_guests
print("Eggs needed:", eggs_needed)
print("Cheese needed:", cheese_needed)

""" Exercise 3 """

total_budget = 1000
daily_cost = 150
trip_length = 5
remaining_budget = total_budget - (daily_cost * trip_length)
print("Remaining budget:", remaining_budget)

""" Exercise 4 """

def calculate_price(cost, tip):
    total = cost + (cost * tip)
    return total

print("Total price with tip:", calculate_price(50, 0.15))

""" Exercise 5 """

def calculate_change(purchase_price, amount_paid):
    change = amount_paid - purchase_price
    return change

print("Change:", calculate_change(30, 50))

""" Exercise 6 """

def minutes_til_midnight(hour, minute):
    total_minutes = 24 * 60 - (hour * 60 + minute)
    return total_minutes

print("Minutes till midnight:", minutes_til_midnight(22, 30))
