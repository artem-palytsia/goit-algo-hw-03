import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1000:
        return []
    list = []
    while len(list)<quantity:
        number=random.randint(min, max)
        if number not in list:
            list.append(number)
    return sorted(list)

print(get_numbers_ticket(25, 300, 6))