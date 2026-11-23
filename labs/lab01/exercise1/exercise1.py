# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km, budget):
    total_km = one_way_km * 2 
    litres_needed = total_km / 10 
    total_cost = litres_needed * 2.00
    if total_cost <= budget:
        return True
    else:
        return False
