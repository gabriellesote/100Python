"""
Crie um programa que peça ao usuário para digitar o comprimento de
dois lados de um triângulo retângulo. Em seguida, o programa deve
calcular e mostrar o comprimento da hipotenusa.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.

"""
import math

print("Determinando os catetos de um triângulo retângulo")
cateto1 = float(input("Comprimento 1: "))
cateto2 = float(input("Comprimento 2: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"Hipotenusa: {hipotenusa}")
