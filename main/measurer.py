#!/usr/bin/env python3

import sys
import time
from code import Mcarlo, binary_search, binary_search_by_recursion, quicksort, fibo, Fibonacci


def measurer(algoritmo: object, repeticoes: int) -> float:

    comeco = time.thread_time()
    for _ in range(repeticoes):
        algoritmo()

    return (time.thread_time() - comeco)/repeticoes


if __name__ == '__main__':

    if sys.argv[1] == "MonteCarlo":
        tempo = measurer(algoritmo=Mcarlo, repeticoes=int(sys.argv[2]))
    elif sys.argv[1] == "BuscaBinaria":
        tempo = measurer(algoritmo=binary_search, repeticoes=int(sys.argv[2]))
    elif sys.argv[1] == "BuscaBinariaRecursiva":
        tempo = measurer(algoritmo=binary_search_by_recursion, repeticoes=int(sys.argv[2]))
    elif sys.argv[1] == "QuickSort":
        pass
    elif sys.argv[1] == "SeqFibonacci":
        pass
    elif sys.argv[1] == "SeqFibonacciRecursiva":
        pass
    else:
        tempo = 0.00

    print(f"{tempo:.4f}")