""" Leia um numero real. Se o numero for positivo imprima a raiz quadrada. 
Do contrário, imprima o numero ao quadrado. """

from math import sqrt
num = float(input("Digite um número qualquer: "))
if num > 0:
    print(f"A raiz quadrada desse número é: {sqrt(num)}")
else:
    print(f"O número ao quadrado desse número é: {num*num}")
