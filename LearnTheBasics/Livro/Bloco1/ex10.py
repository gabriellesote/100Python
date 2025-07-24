"""
(Difícil) Crie um programa que peça ao usuário para digitar três
números (A, B e C). Em seguida, o programa deve calcular e mostrar os
valores das raízes da seguinte equação, usando a fórmula de Bhaskara:

Ax² + Bx + C = 0

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 44).
Edição do Kindle.

"""
import math

a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))

delta = math.pow(b, 2) - (4 * a * c)
print(delta)

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

baskhara_positive = (a * x1**2) + (b * x1) + c
baskhara_negative = (a * x2**2) + (b * x2) + c

print(f"x1 = {round(x1)}\n"
      f"x2 = {round(x2)}\n")
