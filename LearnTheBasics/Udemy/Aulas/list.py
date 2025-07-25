"""
# Podemos Facilmente checar se determinado valor está contido na lista
# if 8 in lista5:
# 	print("Encontrei o número 8")
# else:
# 	print("Não encontrei o número 8")


# if 'e' in lista6:
#     print("Encontrei a letra e")

# # Podemos facilmente ordenar uma lista
# print(lista1)
# lista1.sort()
# print(lista1)

# #Podemos facilmete contar o número de corrências d eum valor em uma lista:

# print(lista1.count(1))
# print(lista6.count('e'))

# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append()
OBS: Com append, podemos adicionar apenas 1 elemento por vez 

print(lista1)
lista1.append(1)
print(lista1)
# Porém podemos adicionar uma lista dentro de outra lista. Porque podemos colocar qualquer tipo de dado, contanto que seja uma unidade.
lista1.append([9,5,6])
print(lista1)

if [9, 5, 6] in lista1:
    print("Encontrei!!")

# 
lista1.extend([1,2,3])
print(lista1)


lista1.insert(2, 'novo valor')
print(lista1)

lista7 = lista1 + lista2 + lista5
print(lista7)


"""

lista1 = [1,2, 3, 5, 7, 0, 2]
lista2 = ['g', 'a', 'b', 'i']
lista3 = []
lista4 = [1, 3, 'as']
lista5 = list(range(11))
lista6 = list("Gabrielle Soares")

lista1 = lista1 + lista2
print(lista1)
