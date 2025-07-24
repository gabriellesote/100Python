"""
Crie um programa que peça ao usuário para digitar o raio de um
círculo. Em seguida, o programa deve calcular e mostrar a área e o
comprimento do círculo.

área (A) = π * raio² e comprimento (C) = 2 * π * raio

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 45).
Edição do Kindle.

"""
import math

raio = float(input("Digite um raio de um circulo: "))

area = math.pi * raio**2
comprimento = 2 * math.pi * raio

print(f"Raio: {raio:.2f}\n"
      f"Área: {area:.2f}\n"
      f"Comprimento: {comprimento:.2f}")
