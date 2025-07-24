"""
Crie um programa que peça ao usuário para digitar um ângulo entre 0 e
360 graus.
Em seguida, o programa deve calcular e mostrar o seno, cosseno e
tangente desse número.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 44)
Edição do Kindle.

"""
import math

x = float(input("Digite um angulo entre 0° e 360° "))
x2 = math.radians(x)
seno = math.sin(x2)
cosseno = math.cos(x2)
tangente = math.tan(x2)

print(f"{x} = {x2}\n"
      f"Seno: {round(seno, 2)}\n"
      f"Cosseno: {round(cosseno, 2)}\n"
      f"Tangente: {round(tangente, 2)}")

# MO LEMBRETE atan != tan
