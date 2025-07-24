"""
Sua solução recebeu Runtime Error provavelmente por uma das seguintes causas:

    Você tentou acessar uma variável não definida;
    Você definiu um array ou vetor com menos capacidade que o requisitado pelo problema;
    Você está tentando acessar uma posição inválida em memória.

Preste atenção a descrição do problema e atente para sua solução para corrigí-la!
Runtime Error

File "/judge/judge-d9829f0bb4584e91a5f794d0720c27eb.d/Main.py", line 8
    def bee2006():
IndentationError: unexpected indent

"""


# def bee2006():
#     tipo_cha = int(input())
#     contador = 0
    
#     if tipo_cha > 4 or 1 > tipo_cha:
#         return

#     try:
#         for i in range(5):
#             resposta = int(input())
#             if resposta > 4 or 1 > resposta:
#                 return
        
#             if resposta == tipo_cha:
#                 contador += 1
#     except:
#         message = "Deu erro!"
#         return message
#     else:
#         print(contador)
#         return contador

# bee2006

# A lógica do meu código estava correta, porém não atendia as exigencias do beecrowd. Devo me atentar a isso!!

# Solução correta ;/ 
# T = int(input("tipo:"))
# A,B,C,D,E = input().split(' ')
# A = int(A)
# B = int(B)
# C = int(C)
# D = int(D)
# E = int(E)
# numbers = [A,B,C,D,E]
# print(numbers.count(T))
inputs = [i for i in input().split()]

print(inputs)