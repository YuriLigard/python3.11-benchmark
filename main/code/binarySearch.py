from __future__ import annotations

class Binary:

    global sorted_collection
    sorted_collection = [1, 1, 4, 6, 6, 7, 9, 10, 10, 11, 12, 12, 12, 14, 15, 15, 16, 18, 19, 21, 22, 26, 26, 27, 29, 29, 29, 31, 32, 32, 32, 33, 35, 37, 37, 40, 41, 42, 42, 43, 44, 44, 46, 47, 47, 48, 52, 52, 53, 54, 56, 58, 58, 59, 62, 62, 63, 64, 64, 65, 67, 67, 68, 70, 70, 70, 72, 72, 73, 74, 75, 76, 76, 77, 78, 78, 78, 78, 78, 78, 79, 79, 79, 81, 82, 84, 84, 87, 88, 91, 92, 92, 93, 94, 95, 98, 99, 99, 100, 100]

    def __init__(self) -> None:
        self.item: int = 33
        ##

    
    def binary_search(self) -> int | None:

        left = 0
        right = len(sorted_collection) - 1

        while left <= right:
            midpoint = left + (right - left) // 2
            current_item = sorted_collection[midpoint]
            if current_item == self.item:
                return midpoint
            elif self.item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return None


    def binary_search_by_recursion(self, left: int = 0, right: int = len(sorted_collection) - 1) -> int | None:
    
        if right < left:
            return None
    
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == self.item:
            return midpoint
        else:
            if current_item > self.item:
                return __class__.binary_search_by_recursion(self, left=left, right=midpoint-1)
            else:
                return __class__.binary_search_by_recursion(self, left=midpoint+1, right=right)

if __name__ == "__main__":
    #sorted_collection = [1, 1, 4, 6, 6, 7, 9, 10, 10, 11, 12, 12, 12, 14, 15, 15, 16, 18, 19, 21, 22, 26, 26, 27, 29, 29, 29, 31, 32, 32, 32, 33, 35, 37, 37, 40, 41, 42, 42, 43, 44, 44, 46, 47, 47, 48, 52, 52, 53, 54, 56, 58, 58, 59, 62, 62, 63, 64, 64, 65, 67, 67, 68, 70, 70, 70, 72, 72, 73, 74, 75, 76, 76, 77, 78, 78, 78, 78, 78, 78, 79, 79, 79, 81, 82, 84, 84, 87, 88, 91, 92, 92, 93, 94, 95, 98, 99, 99, 100, 100]
    binary = Binary()
    print(binary.binary_search())
    print(binary.binary_search_by_recursion())