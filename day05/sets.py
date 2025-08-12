"""
# Data 12/08/2025 - 15:24 -  Conjuntos (Sets)
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos conjuntos da Matemática

- 
"""

"""
# Prática
# definindo um conjunto
# Forma1:

s = set({1,2,3,4,5,5,2,3}) 
print(s)

#forma 2 - mais comum

f = {1,2,3,4,5,6,7,77,7}
print(f)

p = set('gabi')
print(p)

if 3 in f:
    print("Tem o 3")
else:
    print("Não tem o 3")
    
# Além de não ter valores duplicados, não tem ordem

lista = [99,2,34,23,12,1,44,5]
print(f"Lista: {lista}")

tupla = (99,2,34,23,12,1,44,5)
print(f"Tupla: {tupla}")

dic = {}.fromkeys(lista, 'dict')
print(f"Dicionário: {dic}")

conjunto = {99,2,34,23,12,1,44,5}
print(f"Conjunto: {conjunto}")

cidades = [ 'BH', 'SP', 'CG', 'CUI', 'CG', 'SP', 'CUI']
print(cidades)

print(len(cidades))

print(set(cidades))
print(len(set(cidades)))


# Adicionando elementos em um conjunto 

s = {1,2,3}

s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorar e não é adicionado

print(s)


#Remover elementos 
s = {1,2,3}
print(s)

#forma 1
s.remove(3)
print(s)
# Caso tenmtar remover um valor que não existe, dará keyerror. Não retorna nenhum valor.

#forma 2
s.discard(1)
print(s)
# Caso tentar remover um valor que não existe, não acontece nada. 

# Copiando 
s = {1,2,3,4,5}

# Forma 1  -  Deep copy

novo = s.copy()
print(novo)

novo.add(6)
print(novo)


# Forma 2 - Shallow copy

new = s
print(s)
print(new)

new.add(7)
print(s)
print(new)

# Podemos remover todos os itens de um conjunto

s = {1,3,4}
s.clear()




# União
# Forma 1
# unicos = est_py.union(est_jav)
# print(unicos)

# Forma 2
# unicos = est_jav | est_py
# print(unicos)





# Interseção 
# Forma 1 

ambos = est_py.intersection(est_jav)
print(ambos)

# Forma 2  - Utilizando o &
ambos2 = est_jav & est_py
print(ambos2)




est_py = {'Marcos', 'Gabriel', 'Maria', 'Roberto', 'Alice', 'Patricia' }
est_jav = {'Marcos', 'Gabriel', 'Rodrigo', 'Jose', 'Alice', 'Patricia', 'Marcelo' , 'Manuel', 'Patrick'}

# Diferença
# Forma 1 

so_python = est_py.difference(est_jav)
print(so_python)
so_java = est_jav.difference(est_py)
print(so_java)

# forma 2 - utilizando o -
only_py = est_py - est_jav
print(only_py)
only_java = est_jav - est_py
print(only_java)


s = {1,2,3,4,5,5}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""

# Fim de estudo - 17:47 