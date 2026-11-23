# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participants, tent_capacity, tent_price):
    tents_needed = math.ceil(participants/tent_capacity)
    total_cost=tents_needed*tent_price
    return total_cost