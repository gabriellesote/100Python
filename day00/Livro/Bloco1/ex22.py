"""

Crie um programa que calcule e mostre o perímetro de um círculo dado
o seu raio como entrada.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.
"""
import math

raio = float(input("Raio do circulo: "))
perimetro = raio * 2 * math.pi

print(f"Perímetro: {perimetro:.2f}")
