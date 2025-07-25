"""
(Difícil) Crie um programa que peça ao usuário para digitar o
valor inicial de um investimento, a taxa de juros mensal e o número
de meses que o valor ficou investido. Em seguida, o programa deve
calcular e mostrar o valor final do investimento, considerando o uso
de juros compostos.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 47). Edição do Kindle.

"""

investimento_inicial = float(input("Valor inicial do investimento: "))
juros_mensal = float(input("Taxa de juros mensal: "))
qnt_meses = float(input("Quantidade de meses que ficou investido: "))

montante = investimento_inicial * (1 + (juros_mensal / 100))**qnt_meses

print(f"Montante: R${montante:.2f}")
