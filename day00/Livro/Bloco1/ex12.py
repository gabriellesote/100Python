"""
Crie um programa que peça ao usuário para digitar as dimensões de um
retângulo (largura e altura). Em seguida, o programa deve calcular e
mostrar a área e o perímetro desse retângulo.
A = b * h
P = 2 * (b + h)
Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 45). Edição do Kindle.

"""

retangulo_largura = float(input("Insira a largura do retangulo: "))
retangulo_altura = float(input("Insira a altura do retangulo: "))

area = retangulo_largura * retangulo_altura
perimetro = 2 * (retangulo_altura + retangulo_largura)

print(f"Altura: {retangulo_altura} e Largura: {retangulo_largura}\n"
      f"Área: {area:.2f}\n"
      f"Perímetro: {perimetro:.2f}")
