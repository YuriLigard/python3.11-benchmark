from __future__ import annotations
from random import randrange

def quicksort(collection: list[int] = [99, 78, 12, 98, 29, 77, 46, 1, 12, 26, 7, 99, 78, 4, 76, 84, 65, 78, 68, 59, 92, 31, 62, 10, 94, 79, 75, 47, 29, 67, 33, 9, 22, 64, 15, 81, 32, 53, 91, 6, 43, 48, 100, 78, 100, 42, 47, 70, 88, 54, 79, 79, 82, 32, 52, 93, 72, 44, 44, 95, 32, 12, 21, 29, 52, 78, 40, 63, 58, 19, 35, 72, 37, 76, 70, 58, 10, 87, 56, 14, 11, 41, 62, 27, 6, 15, 74, 16, 92, 37, 73, 1, 67, 26, 64, 84, 18, 42, 78, 70]) -> list:
    
    if len(collection) < 2:
        return collection
    
    pivot_index = randrange(len(collection))
    pivot = collection[pivot_index]

    greater: list[int] = []
    lesser: list[int] = []

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1:]:
        (greater if element > pivot else lesser).append(element)

    return quicksort(lesser) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    unsorted = [99, 78, 12, 98, 29, 77, 46, 1, 12, 26, 7, 99, 78, 4, 76, 84, 65, 78, 68, 59, 92, 31, 62, 10, 94, 79, 75, 47, 29, 67, 33, 9, 22, 64, 15, 81, 32, 53, 91, 6, 43, 48, 100, 78, 100, 42, 47, 70, 88, 54, 79, 79, 82, 32, 52, 93, 72, 44, 44, 95, 32, 12, 21, 29, 52, 78, 40, 63, 58, 19, 35, 72, 37, 76, 70, 58, 10, 87, 56, 14, 11, 41, 62, 27, 6, 15, 74, 16, 92, 37, 73, 1, 67, 26, 64, 84, 18, 42, 78, 70]
    print(quicksort(collection=unsorted))
    