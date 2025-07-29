"""
1. Faça um programa que determine e mostre os cinco primeiros
múltiplos de 3, considerando números
maiores que 0.
2. Faça um programa que utilize o comando while para mostrar na tela
uma contagem regressiva, iniciando
em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
3. Faça um programa que declare um inteiro, inicialize-o com 0,
incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil)

"""

# n = 3

# for i in range(1, 20):
#     if i % n == 0:
#         print(i)


# n = 10
# while n != -1:
#     print(n)
#     n = n - 1
# print("FIM!")

# n = 0 

# while n != 101000:
#     print(n)
#     n = n + 1000


# REsoluções do professor:

# Atividade 1:
# contador = 0
# indice = 1
# while contador < 5:
#     if indice % 3 == 0:
#         contador += 1
#         print(f"{indice} é multiplo de 3")
#     indice += 1


# atividade 3:
# for i in range(0, 100001, 1000):
#     print(i)