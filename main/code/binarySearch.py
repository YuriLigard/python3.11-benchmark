from __future__ import annotations
from distutils.command.build import build
from operator import le
import re

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
    left: int, 
    right: int
) -> int | None:

    if right < left:
        return None
    
    midpoint = left + (right - left) // 2
    current_item = sorted_collection[midpoint]
    if current_item == item:
        return midpoint
    else:
        if current_item > item:
           return binary_search_by_recursion(sorted_collection=sorted_collection, item=item, left=left, right=midpoint-1)
        else:
           return binary_search_by_recursion(sorted_collection=sorted_collection, item=item, left=midpoint+1, right=right)

if __name__ == "__main__":
    sorted_collection = [0, 2, 6, 10, 14, 22, 30, 58, 26, 100, 125]
    a = binary_search_by_recursion(sorted_collection = sorted_collection, item=100, left=0, right=(len(sorted_collection) - 1))
    print(a)