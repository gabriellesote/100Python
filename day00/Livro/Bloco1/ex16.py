"""
(Difícil) Crie um programa que peça ao usuário para digitar a massa e
a aceleração de um objeto. Em seguida, o programa deve calcular e
mostrar a força resultante.
F = m * a
Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 45). Edição do Kindle.


"""

massa = float(input("Massa: "))
aceleracao = float(input("Aceleração: "))

forca = massa * aceleracao

print(f"Força: {forca:.0f}N")
