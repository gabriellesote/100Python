"""
Crie um programa que peça ao usuário para digitar a velocidade
inicial, a velocidade final e o tempo de transição de uma velocidade
para a outra. Em seguida, o programa deve calcular e mostrar a
aceleração.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 46). Edição do Kindle.

"""
vel_inicial = float(input("Velocidade inicial: "))
vel_final = float(input("Velocidade final: "))
tempo_transicao = float(input("Tempo de transição entre velocidades: "))

delta_velocidade = (vel_final - vel_inicial)
aceleracao = delta_velocidade / tempo_transicao

print(f"Aceleração: {aceleracao:.1f}")
