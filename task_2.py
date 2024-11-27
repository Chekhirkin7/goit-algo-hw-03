import random

def get_numbers_ticket(min, max, quantity):
	min = int(min)
	max = int(max)
	quantity = int(quantity)
	if (min >= 1 and max <= 1000) and (max > 0 and min > 0) and min < max and (max - min > quantity):
		ticket = random.sample(range(min, max+1), quantity)
		sorted_ticket = ticket.sort()
	else:
		ticket = []

	return ticket

print(get_numbers_ticket(-10,14,6))