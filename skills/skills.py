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
trip_length = total_budget // daily_cost
print("Trip length:", trip_length)
