from __future__ import annotations
from operator import le

def binary_search(sorted_collection: list[int] = [0, 2, 6, 10, 14, 22, 30, 58, 26, 100, 125], item: int = 6) -> int | None:

    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def binary_search_by_recursion(
    sorted_collection: list[int], 
    item: int, 
    left: int = 0, 
    right: int = -1
) -> int | None:

    if left == 0:
        right = len(sorted_collection)
    
    if left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            binary_search_by_recursion(sorted_collection=sorted_collection, )