"""
Crie um programa que calcule e mostre o volume de uma esfera dado o
seu raio como entrada.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.

"""
import math

raio = float(input("Raio da esfera: "))
volume = (4/3) * math.pi * raio**3

print(f"Volume da esfera: {volume:.2f}")
