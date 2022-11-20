from __future__ import annotations


def fibo(end: int) -> list:

    sequence: list[int] = [0, 1]

    if end <= 1:
        return end
    
    index = 1

    while sequence[index] < end:
        sequence.append(sequence[index-1] + sequence[index])
        
        index+=1

    return sequence


class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
       
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


if __name__ == "__main__":
    fibo(20)
    fibonacci = Fibonacci()
    fibonacci.get(20)

    
        