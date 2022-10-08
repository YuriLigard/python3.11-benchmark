import random



def Buffon(quantAgulha: int):

    quantAgulhaDentro = 0

    equacaoCircunf = lambda x,y: x**2 + y**2     # Considerando que o centro da circunferência esteja em (0,0)

    for _ in range(0, quantAgulha):
        x, y = (random.uniform(-1, 1) for v in range(2))
        if equacaoCircunf(x, y) <= 1:
            quantAgulhaDentro +=1

    estimativaPi = (4 * quantAgulhaDentro) / quantAgulha





    