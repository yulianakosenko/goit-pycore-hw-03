import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    # контроль заданих параметрів
    if not (1 <= min <= max <= 1000 and quantity <= (max - min + 1)):
        return []

    # Generate a random list of numbers
    random_numbers = random.sample(range(min, max + 1), quantity)
    # Sort the list
    
    return sorted(random_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)