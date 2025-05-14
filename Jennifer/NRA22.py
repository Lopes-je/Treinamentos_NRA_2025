import matplotlib.pyplot as plt
import numpy as np
import random as r

lista = []
for _ in range (20):
   num = r.randint(1,100)
   lista.append(num)

plt.title('Gráfico')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.plot(lista)

plt.show()