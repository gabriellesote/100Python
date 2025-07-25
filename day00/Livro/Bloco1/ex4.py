"""Exercício1.4::Crie um programa que peça ao usuário para digitar
seu peso e sua altura.
Em seguida, calcule o índice de massa corporal (IMC) e imprima o resultado.
A fórmula do IMC é:

IMC = peso/ altura²

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 43).
Edição do Kindle.
"""
import math

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / math.pow(altura, 2)

print(round(imc, 1))
