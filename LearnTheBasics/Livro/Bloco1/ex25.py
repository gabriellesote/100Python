"""
Crie um programa que leia o nome, o salário e o valor do imposto de
uma pessoa como entrada e imprima, ao fim, uma saída no seguinte
formato: "Fulano tem um salário líquido de R$ 1.800,00.". Observe a
formatação do salário.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 47). Edição do Kindle.

"""

import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

nome = input("Nome: ")
salario_entrada = float(input("Insira seu salário Bruto: "))
valor_imposto = float(input("Valor do imposto: "))
salario_liquido = locale.currency((salario_entrada - valor_imposto),
                                  grouping=True)

print(f"{nome} tem um salário líquido de R${salario_liquido}")
