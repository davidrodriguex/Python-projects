"""Leia um numero fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
Se o número for negativo, mostre uma mensagem dizendo que o numero é inválido."""

import math
num = int(input("Digite um número inteiro: "))
if num >= 0:
    print("A raiz quadrada desse número é: {}".format(math.sqrt(num)))
else:
    print("Este número é inválido.")
