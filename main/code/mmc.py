import random


def Mcarlo(needles = 2000):

    needlesInside = 0

    circumfEquantion = lambda x,y: x**2 + y**2     # Considerando que o centro da circunferência esteja em (0,0)

    for _ in range(0, needles):
        x, y = (random.uniform(-1, 1) for v in range(2))
        if circumfEquantion(x, y) <= 1:
            needlesInside +=1

    approximationPi = (4 * needlesInside) / needles





    