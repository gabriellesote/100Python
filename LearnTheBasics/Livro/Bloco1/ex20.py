"""
Crie um programa que peça ao usuário para digitar a distância
percorrida por um objeto e o tempo gasto no trajeto. Em seguida, o
programa deve calcular e mostrar a velocidade média do objeto.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.
"""

print("Velocidade km/h")

distancia = float(input("Distancia pecorrida (em km): "))
tempo_gasto = int(input("Tempo gasto (em horas): "))

velocidade_media = distancia / float(tempo_gasto)

print(f"Velociade media: {velocidade_media:.2f}")
