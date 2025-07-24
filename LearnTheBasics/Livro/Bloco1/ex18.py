"""
Crie um programa que peça ao usuário para digitar o valor da medida
de um ângulo em radianos. Em seguida, o programa deve calcular e
mostrar o valor desse ângulo em graus.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.

"""
import math

radianos = float(input("Ângulo em radianos: "))
graus = radianos * (180 / math.pi)

print(f"Radianos: {radianos}\n"
      f"Graus: {graus:.2f}\n")
