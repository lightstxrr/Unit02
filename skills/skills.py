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

""" Exercise 7 """

def apply_discount(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price


def apply_tax(price, sales_tax):
    taxed_price = price + (price * sales_tax)
    return taxed_price


def final_price(price, discount, sales_tax):
    discounted_price = apply_discount(price, discount)
    total_price = apply_tax(discounted_price, sales_tax)
    return total_price


print(final_price(85, 0.15, 0.08))

""" Exercise 8 """

score = 100
bonus = 25
penalty = 15

final_score = score + bonus - penalty

print(final_score)

recipe_serves = 5
num_guests2 = 10
cups_flour = 3

flour_needed = cups_flour / recipe_serves * num_guests2

print(flour_needed)