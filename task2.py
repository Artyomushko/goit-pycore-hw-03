import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if quantity > max - min + 1 or min > max:
        print("Impossible")
        return []

    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))

    return list(result)

print(get_numbers_ticket(10, 20, 11))
print(get_numbers_ticket(10, 20, 20))
print(get_numbers_ticket(20, 20, 1))
print(get_numbers_ticket(21, 20, 1))
print(get_numbers_ticket(10, 20, 5))