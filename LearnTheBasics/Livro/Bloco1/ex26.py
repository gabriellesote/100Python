"""

(Difícil) Crie um programa que peça ao usuário para digitar a
altitude inicial de um objeto em queda livre a partir do repouso. Em
seguida, o programa deve calcular e mostrar o tempo que o objeto leva
para atingir o solo, desconsiderando a resistência do ar.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 47). Edição do Kindle.
"""
import math

altitude_inicial = float(input("Altitude inicial: "))
tempo_queda = math.sqrt((2 * altitude_inicial / 9.8))
print(f"Tempo de queda: {tempo_queda:.2f}")
