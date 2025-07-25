"""
Crie um programa que tenha dois conjuntos de 5 números quaisquer e
combine-os usando as operações de união, interseção e diferença,
apresentando os resultados de cada operação.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (pp. 47-48). Edição do Kindle.

"""


conjunto1 = {2, 3, 4, 5, 6}
conjunto2 = {2, 3, 7, 8, 9, 10}

uniao = conjunto1 | conjunto2
intersecao = conjunto1 & conjunto2
diferenca = conjunto1 - conjunto2

print(f"{conjunto1}\n"
      f"{conjunto2}\n"
      f"União: {uniao}\n"
      f"Interseção: {intersecao}\n"
      f"Diferença: {diferenca}\n")
