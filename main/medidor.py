import sys, os
import time
from main.py37_38_39_310_311 import Buffon


def medidor(algoritmo: object, repeticoes: int) -> float:

    comeco = time.thread_time()
    for _ in range(repeticoes):
        algoritmo(5000)

    return (time.thread_time() - comeco)/repeticoes


if __name__ == '__main__':

    if sys.argv[1] == 'Buffon':
        tempo = medidor(algoritmo=Buffon, repeticoes=int(sys.argv[2]))
    elif sys.argv[1] == 'o':
        #tempo = medidor(algoritmo=o, repeticoes=int(sys.argv[2]))
        pass

    

    print(f"{tempo:.4f}")