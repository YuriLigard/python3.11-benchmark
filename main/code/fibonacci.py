from __future__ import annotations


class Fibonacci:

    def __init__(self) -> None:
        self.sequence: list[int] = [0, 1]
        
    def fibonacci(self, end: int) -> list:
        
        if end <= 1:
            return end
        
        index = 1

        while self.sequence[index] < end:
            self.sequence.append(self.sequence[index-1] + self.sequence[index])
        
            index+=1

        return self.sequence
        
    def fibonacci_recursion(self, index: int) -> list:
       
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


if __name__ == "__main__":
    fibonacci = Fibonacci()
    print("-->",fibonacci.fibonacci(20))
    print("-->",fibonacci.fibonacci_recursion(20))

    
        