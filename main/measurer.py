#!/usr/bin/env python3

import sys
import time
from code import Mcarlo, binary_search, binary_search_by_recursion, quicksort, fibo, Fibonacci


def measurer(algoritmo: object, loop: int) -> float:

    start = time.thread_time()
    for _ in range(loop):
        algoritmo()

    return (time.thread_time() - start)/loop


if __name__ == '__main__':

    if sys.argv[1] == "MonteCarlo":
        tm = measurer(algoritmo=Mcarlo, loop=int(sys.argv[2]))
    elif sys.argv[1] == "BuscaBinaria":
        tm = measurer(algoritmo=binary_search, loop=int(sys.argv[2]))
    elif sys.argv[1] == "BuscaBinariaRecursiva":
        tm = measurer(algoritmo=binary_search_by_recursion, loop=int(sys.argv[2]))
    elif sys.argv[1] == "QuickSort":
        tm = measurer(algoritmo=quicksort, loop=int(sys.argv[2]))
    elif sys.argv[1] == "SeqFibonacci":
        tm = measurer(algoritmo=fibo, loop=int(sys.argv[2]))
    elif sys.argv[1] == "SeqFibonacciRecursiva":
        fibonacci = Fibonacci()
        tm = measurer(algoritmo=fibonacci.get, loop=int(sys.argv[2]))
    else:
        tm = 0.00

    print(f"{tm:.4f}")
