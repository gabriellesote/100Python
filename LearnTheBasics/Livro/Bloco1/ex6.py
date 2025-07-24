"""
Crie um programa que peça ao usuário para digitar um número.
Em seguida, o programa deve calcular e mostrar a raiz quadrada desse número.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 44).
Edição do Kindle.

"""
import math

x = float(input("Digite um número "))
raiz_quadrada = math.sqrt(x)
print(f"Raiz quadrada de {round(x)} é igual a "
      f"{round(raiz_quadrada, 2)}")
