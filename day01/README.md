# 📜 Listas - Day 001

> Parte mais importante do python

Listas em python funcionam como vetores/ matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO  e também de podermos colocar *qualquer* tipo de dado.

Linguagens C/ Java: Arrays
		- Possuem tamanho e tipo de dado fixo.
	Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.


Já em Python:
- Dinâmico:  Não possui tamanho fixo. Ou seja, podemos criar a lista e simplesmente ir adicionando elementos. Enquanto houver memória disponível, pode adicionar elementos.
- Qualquer tipo de dado:  Não possuem tipo de dado fixo. Ou seja, podemos colocar qualquer tipo de dado.

As listas em python são representadas por colchetes: [ ]

```python
type([])
# Output
# list
```

Exemplos:

```python
lista1 = [1, 3, 5, 7]

lista2 = ['g', 'a', 'b', 'i']

lista3 = []

lista4 = [1, 3, 'as']

lista5 = list(range(11))

lista6 = list("Gabrielle Soares")
# Outputs:
#[1, 3, 5, 7]
#['g', 'a', 'b', 'i']
#[]
#[1, 3, 'as']
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#['G', 'a', 'b', 'r', 'i', 'e', 'l', 'l', 'e', ' ', 'S', 'o', 'a', 'r', 'e', 's']
```
#### List()

Transforma em uma lista. 

```python
lista = list(range(11))
```

# O que podemos fazer?

###  1.Podemos facilmente checar se determinado valor está contido na lista

```python 
if 8 in lista4:
	print("Encontrei o número 8")
else:
	print("Não encontrei o número 8)
```
### 2. Podemos ordenar uma lista

```python
print(lista1)

lista1.sort()

print(lista1)
```

### 3. Podemos facilmente contar o número de ocorrências de um valor em uma lista

```python

```

### 4. Adicionar elementos em uma lista:

Para adicionar elementos em listas, utilizamos a função append()

> OBS: Com append, podemos adicionar apenas 1 elemento por vez

```python
print(lista1)

lista1.append(1)

print(lista1)

## Output:
#[1, 3, 5, 7]
#[1, 3, 5, 7,1]
```

Porém podemos adicionar uma lista dentro de outra lista, e coloca como **elemento único**. Porque podemos colocar qualquer tipo de dado, contanto que seja uma unidade.

```python
lista1.append([9,5,6])

print(lista1)
#Output
# [1, 1, 1, 3, 5, 7, 0, 2, 1, [9, 5, 6]]
```

Funciona também no If:
```python
if [9, 5, 6] in lista1:
    print("Encontrei!!")
```

#### Extend()

Adiciona elementos da lista um a um:
```python
lista1.extend([1,2,3])

print(lista1)
#output
#[1, 1, 1, 3, 5, 7, 0, 2, 1, [9, 5, 6], 1, 2, 3]
```

Não aceita valor único, aceita apenas os objetos inteiráveis:
- Lista
- String


#### Tanto o append() quanto o extend() atribuem valores ao final da lista

### 5. Podemos inserir um novo elemento informado a posição do índice

```python
lista1 = [1,2, 3, 5, 7, 0, 2]
lista1.insert(2, 'novo valor')
print(lista1)
#output
#[1, 1, 'novo valor', 1, 3, 5, 7, 0, 2]
```

> Isso não substitui o valor inicial! O mesmo será descolado para a direita da lista.


### 6. Podemos facilmente juntar duas listas

> Faz o mesmo do extends()

Exemplo criando uma nova lista:
```python
lista7 = lista1 + lista2 + lista5

print(lista7)
[1, 2, 3, 5, 7, 0, 2, 'g', 'a', 'b', 'i', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Exemplo sem criar uma nova lista:
```python
lista1 = lista1 + lista2
print(lista1)
```

for i in range(size):

               print(word1[i])

            print(newword)



### 7. Podemos remover elementos com `remove()`

> Remove **apenas a primeira ocorrência** do valor especificado.

```python
lista = [1, 2, 3, 2, 4]
lista.remove(2)
print(lista)
# Output: [1, 3, 2, 4]
```

Se o valor não existir, lança erro:

```python
lista.remove(10)
# ValueError: list.remove(x): x not in list
```

---

### 8. Podemos remover elementos com `pop()`

> Remove e retorna o último elemento (ou o índice informado).

```python
lista = [1, 2, 3, 4]
valor = lista.pop()
print(valor)   # 4
print(lista)   # [1, 2, 3]
```

Com índice:

```python
valor = lista.pop(0)
print(valor)   # 1
print(lista)   # [2, 3]
```

---

### 9. Podemos remover todos os elementos com `clear()`

```python
lista = [1, 2, 3]
lista.clear()
print(lista)
# Output: []
```

---

### 10. Podemos repetir elementos com o operador `*`

```python
lista = [1, 2]
nova = lista * 3
print(nova)
# Output: [1, 2, 1, 2, 1, 2]
```

---

### 11. Podemos converter string em lista com `list()`

```python
texto = "Python"
lista = list(texto)
print(lista)
# Output: ['P', 'y', 't', 'h', 'o', 'n']
```

---

### 12. Podemos acessar elementos por índice

```python
lista = [10, 20, 30]
print(lista[0])  # 10
print(lista[-1]) # 30 (último)
```

---

### 13. Podemos fatiar (slicing) listas

```python
lista = [0, 1, 2, 3, 4, 5]
print(lista[1:4])    # [1, 2, 3]
print(lista[:3])     # [0, 1, 2]
print(lista[::2])    # [0, 2, 4]
print(lista[::-1])   # [5, 4, 3, 2, 1, 0] (inverte)
```

---

### 14. Podemos substituir elementos diretamente

```python
lista = [1, 2, 3]
lista[1] = 99
print(lista)
# Output: [1, 99, 3]
```

---

### 15. Podemos iterar sobre a lista com `for`

```python
lista = ['a', 'b', 'c']
for letra in lista:
    print(letra)
```

Com índice:

```python
for i in range(len(lista)):
    print(f"{i}: {lista[i]}")
```

---

### 16. Podemos usar `enumerate()` para iterar com índice e valor

```python
for i, valor in enumerate(['a', 'b', 'c']):
    print(f"Índice {i} = {valor}")
```

---

### 17. Podemos verificar o tamanho da lista com `len()`

```python
lista = [1, 2, 3, 4]
print(len(lista))
# Output: 4
```

---

### 18. Podemos contar quantas vezes um valor aparece com `count()`

```python
lista = [1, 2, 2, 3, 2]
print(lista.count(2))
# Output: 3
```

---

### 19. Podemos descobrir o índice de um valor com `index()`

```python
lista = [10, 20, 30]
print(lista.index(20))
# Output: 1
```

> Se o valor não estiver presente, dá erro.

---

### 20. Podemos copiar uma lista com `copy()`

```python
lista1 = [1, 2, 3]
lista2 = lista1.copy()
print(lista2)
# Output: [1, 2, 3]
```

---

### 21. Podemos usar listas aninhadas (listas dentro de listas)

```python
matriz = [[1, 2], [3, 4]]
print(matriz[0])     # [1, 2]
print(matriz[0][1])  # 2
```

---

### 22. Podemos usar compreensão de listas (list comprehension)

Forma rápida e elegante de criar listas.

```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)
# Output: [0, 2, 4, 6, 8]
```

Com transformação:

```python
quadrados = [x**2 for x in range(5)]
print(quadrados)
# Output: [0, 1, 4, 9, 16]
```


### 23. Operar listas

```python
sum(lista)  # soma
max(lista)  # maximo valor
min(lista)  # minimo valor
len(lista)  # tamanho da lista


```

### 24. Desempacotamento de lista 

```python
lista = [1,2,3,4]
num1,num2,num3,num4 = lista

```

> OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError

### 25. Copiando uma lista para outra (Bastante cobrado)
Shallow copy e Deep Copy

```python
lista = [1,2,3]
print(lista)

nova = lista.copy()

nova.append(4)
print(lista)
print(nova)
# [ 1,2,3]
# [1,2,3]
# [1,2,3,4]

```

Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente independentes, modificando uma lista, não afeta a outra.  
Isso em Python é chamado de Deep COpy ( cópia profunda)


##### Forma 2 - Shallow Copy

```python

lista = [1,2,3]
print(lista)

nova = lista
print(nova)
nova.append(4)
print(lista)
print(nova)

#
#
```

Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar modificações em uma das listas, essa modificação se refletiu em ambas as listas
isso em Python é chamado de Shallow Copy
