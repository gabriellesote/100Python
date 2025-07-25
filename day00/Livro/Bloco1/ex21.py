"""
(Difícil) Crie um programa que peça ao usuário para digitar a
distância percorrida, o tempo gasto e a aceleração de um objeto. Em
seguida, o programa deve calcular e mostrar a velocidade inicial e final.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.

"""


distancia_percorrida = float(input("Distancia pecorrida: "))
tempo_gasto = float(input("Tempo gasto: "))
aceleracao = float(input("Aceleração: "))

v0 = (distancia_percorrida / tempo_gasto) - ((aceleracao *
                                             tempo_gasto) / 2)

v1 = v0 + aceleracao * tempo_gasto

print(f"Velocidade inicial (v0): {v0}\n"
      f"Velocidade final (v1): {v1}")
