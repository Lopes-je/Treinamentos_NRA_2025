import numpy as np
import random

numero = []

for _ in range (9):
    num = np.random.randint(1,100)
    numero.append(num)



A = np.array(numero).reshape(3,3)

numero1 = []

for _ in range (9):
    num = np.random.randint(1,100)
    numero1.append(num)


B = np.array(numero1).reshape(3,3)

print("Matriz A: \n", A, '\n')
print('Matriz B: \n', B , '\n')

C = A+B

print('Matriz C: \n', C, '\n')

D = A@B
print('Produto A com B: \n', D, '\n')

E = A*B
print('Produto A com B (elemento com elemento):\n', E, '\n')
