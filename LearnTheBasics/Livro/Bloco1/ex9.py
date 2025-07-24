"""
Crie um programa que peça ao usuário para digitar dois números quaisquer.
Em seguida, o programa deve calcular e mostrar a potência do primeiro
número pelo segundo.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 44).
Edição do Kindle.
"""
import math

x = int(input("Numero: "))
y = int(input("Numero: "))

potencia = math.pow(x, y)

print(f"Potencia: x^y = {potencia}")
