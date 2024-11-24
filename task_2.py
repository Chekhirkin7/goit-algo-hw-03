import random

def get_numbers_ticket(min, max, quantity):
	min = int(min)
	max = int(max)
	quantity = int(quantity)
	if min >= 1 and max <= 1000:
		ticket = random.sample(range(min, max+1), quantity)
		sorted_ticket = ticket.sort()
	else:
		print("Введіть числа від 1 до 1000")
		return None

	return print(ticket)

get_numbers_ticket(1,49,3)