#!/usr/bin/env python3

import sys, os
import time
from code import Mcarlo


def medidor(algoritmo: object, repeticoes: int) -> float:

    comeco = time.thread_time()
    for _ in range(repeticoes):
        algoritmo()

    return (time.thread_time() - comeco)/repeticoes


if __name__ == '__main__':

    if sys.argv[1] == 'Mcarlo':
        tempo = medidor(algoritmo=Mcarlo, repeticoes=int(sys.argv[2]))
    elif sys.argv[1] == 'o':
        #tempo = medidor(algoritmo=o, repeticoes=int(sys.argv[2]))
        pass

    print(f"{tempo:.4f}")
