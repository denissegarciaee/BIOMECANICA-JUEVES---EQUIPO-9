from multiprocessing import Pool
from random import randint
import matplotlib.pyplot as plt

width = 10000
heigth = width
radio = width
npuntos = 0
ndentro = 0
radio2 = radio * radio
replicas = 1000
promediopi = []

if __name__ == '__main__':
    with Pool(4) as p:
        for j in range(replicas):
            for i in range(1, 100000):
                x = randint(0, width)
                y = randint(0, width)
                npuntos += 1
                if x * x + y * y <= radio2:
                    ndentro += 1
                pi = ndentro * 4 / npuntos
                promediopi.append(pi)
plt.xlim(0,1000)
plt.ylim(2.12,5)
plt.plot(promediopi)
plt.xlabel('Número de replicas')
plt.ylabel('Valor de pi')
plt.title('Tarea 3 biomecánica-Equipo 9')
plt.grid()
plt.show()
