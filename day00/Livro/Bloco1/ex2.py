"""
  Exercício 1.2 :: Crie um programa que armazene dois números em
  variáveis separadas e imprima a soma, subtração,
  multiplicação e divisão desses números.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition)
(p. 43). Edição do Kindle.
  """

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print(f"Soma: {soma}\n"
      f"Subtração: {subtracao}\n"
      f"Multiplicação: {multiplicacao}\n"
      f"Divisão: {divisao}")
