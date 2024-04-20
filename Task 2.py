import random

def get_numbers_ticket(minimum, maximum, quantity):
    if minimum <1 or maximum >1000 or quantity < 1 or quantity >(maximum - minimum+1):
        return []
    number_input = set()
    while len(number_input) < quantity:
        number_input.add(random.randint(minimum, maximum))
    return sorted(list(number_input))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


