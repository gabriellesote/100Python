"""
Crie um programa que peça ao usuário para digitar um número inteiro.
Em seguida, o programa deve calcular e mostrar o valor dos inteiros
anterior e posterior a esse número.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 44).
Edição do Kindle.
"""

x = int(input("Digite um número inteiro: "))

anterior = x - 1
posterior = x + 1


print(f"{anterior}, {x}, {posterior}")

# MO REFAZER depois com mais complexidade, usando for()
