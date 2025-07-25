"""
Crie um programa que calcule e mostre a área de um triângulo
retângulo dadas as medidas dos seus catetos como entrada.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 47). Edição do Kindle.

"""

print("Área de um triângulo retângulo")

cateto1 = float(input("Cateto 1: "))
cateto2 = float(input("Cateto 2: "))
area = (cateto1 * cateto2) / 2

print(f"Área do triângulo retângulo: {area}")
