"""
Exercício1.3::Crie um programa que peça ao usuário para digitar
três números, armazenando-os em variáveis distintas.
Em seguida, imprima a média aritmética dos três números.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 43).
Edição do Kindle.
"""
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

media = (n1 + n2 + n3) / 3

print(round(media))
