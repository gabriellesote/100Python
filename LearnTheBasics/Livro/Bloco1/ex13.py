"""
Crie um programa que peça ao usuário para digitar a base e a
altura de um triângulo. Em seguida, o programa deve calcular e
mostrar a área desse triângulo.

Área = (base * altura) / 2

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 45). Edição do Kindle.
"""

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triangulo: "))

area = (base * altura) / 2

print(f"Base: {base} | Altura: {altura}\n"
      f"Área: {area:.1f}cm²")
