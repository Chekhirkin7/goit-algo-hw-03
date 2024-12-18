import random

def get_numbers_ticket(min, max, quantity):
    
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

lottery_numbers = get_numbers_ticket(10,14,3)
print("Ваші лотерейні числа:", lottery_numbers)
