#!/usr/bin/env python3

import sys
import time
from code import Mcarlo, quicksort, Binary, Fibonacci


def measurer(algoritmo: object, loop: int) -> float:

    start = time.thread_time()
    for _ in range(loop):
        algoritmo()

    return (time.thread_time() - start)/loop


if __name__ == '__main__':

    if sys.argv[1] == "MonteCarlo":
        tm = measurer(algoritmo=Mcarlo, loop=int(sys.argv[2]))
    elif sys.argv[1] == "BuscaBinaria":
        binary = Binary()
        tm = measurer(algoritmo=binary.binary_search, loop=int(sys.argv[2]))
    elif sys.argv[1] == "BuscaBinariaRecursiva":
        binary = Binary()
        tm = measurer(algoritmo=binary.binary_search_by_recursion, loop=int(sys.argv[2]))
    elif sys.argv[1] == "QuickSort":
        tm = measurer(algoritmo=quicksort, loop=int(sys.argv[2]))
    elif sys.argv[1] == "SeqFibonacci":
        fibonacci = Fibonacci()
        tm = measurer(algoritmo=fibonacci.fibonacci, loop=int(sys.argv[2]))
    elif sys.argv[1] == "SeqFibonacciRecursiva":
        fibonacci = Fibonacci()
        tm = measurer(algoritmo=fibonacci.fibonacci_recursion, loop=int(sys.argv[2]))
    else:
        tm = 0.00

    print(f"{tm:.10f}")
