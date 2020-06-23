import random
def partition(data: list, pivot) -> tuple:
    less, equal, greater = [], [], []
    for element in data:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater

def quick_select(items: list, index: int):
    if index >= len(items) or index < 0:
        return None

    pivot = random.randint(0, len(items) - 1)
    pivot = items[pivot]
    count = 0
    smaller, equal, greater = partition(items, pivot)
    count = len(equal)
    m = len(smaller)

    if m <= index < m + count:
        return pivot
    elif m > index:
        return quick_select(smaller, index)
    else:
        return quick_select(greater, index - (m + count))