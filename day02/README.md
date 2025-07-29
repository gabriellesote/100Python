# 🪐 Tuplas - Day002


Tuplas são bastante parecidas com listas
Existem basicamente duas diferenças básicas:

 1.  As tuplas são representadas por parênteses ()
 
 ```python

	print(type(()))
```

2. As Tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla. 

> Cuidado 1: As tuplas são representadas por () mas veja:

```python
tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))
# cass tuple

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))
# cass tuple
```


> Cuidado 2 : Tuplas com 1 elemento

```python
tupla1 = (6)  
print(tupla1)
print(type(tupla1))
# cass int
```
Não é uma tupla quando tem apenas 1 elemento.

```python
tupla1 = (1,)
print(tupla1)
print(type(tupla1))
# cass tuple
tupla2 = 1,
print(type(tupla2))
# cass tuple
```
Mas esse é uma tupla

Conclusão, tuplas são definidas pela vírgula, e não pelo parênteses.

### Podemos gerar tuplas com range

```python 
tupla = tuple(range(11))
```

### Desempacotamento de tupla 

```python
tupla = (' Gabrielle Soares)
nome, sobrenome = tupla
print(nome)
print(sobrenome)
```

> Gera erro se (ValueError) se colocarmos um número diferente de elementos para desempacotar.


### Métodos para adição e remoção 

Não existem, dado o fato das tuplas serem imutáveis.

Porém da para fazer operações (Soma*, Valor maximo,* valor minimo* e tamanho) 
* Se os valores forem todos inteiros ou reais*,  só conseguimos fazer operações de:
  sum()
  max()
  min()
  Se esses valores forem inteiros ou reais
  - Porém o len() pode ser operado com qualquer tipo de valor


### Concatenação de tuplas

```python
tupla1 = (1,2,3)

print(tupla1)

tupla2 = (3,4,5,6)

print(tupla2)

  

print(tupla1 + tupla2) # tuplas são imutaveis

print(tupla1)

print(tupla2)
```


### Sobrescrever tuplas

Tuplas são imutáveis, mas podemos sobrescrever seus valores

```python
tupla1 = (1,2,3)
tupla2 = (3,4,5,6)


tupla2 = tupla1 + tupla2

print(tupla2)


```

### Verificar se determinado elemento está contido na tupla

```python
tupla1 = (1,2,3)

print( 3 in tupla)
# True
```


### Iterando sobre uma tupla

```python
tupla1 = (1,2,3)

for n in tupla1: 
	print(n)
	
for i, v in enumerate(tupla1): 
	print(i, v)
```

### Contanto elementos dentro de uma tupla


```python
nome = 'gabrielle'
tupla = tuple(nome)

print(tupla.count('e'))
```


### Dicas na utilização de tuplas

Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção
- Meses ( Jan --- Dezembro)

### Acesso a elementos de uma tupla

É semelhante a de uma lista 
```python
print(tupla[1])
```

### Iterar com while

```python 
i = 0
while i in len(tupla):
	print(tupla[i])
	i = i + 1
```

### Verificamos em qual índice um elemento está na tupla

```python 
ṕrint(meses.index('Janeiro'))
```

> OBS: Caso o elemento não exista, será gerado o ValueError

### Slicing

```python
tupla[inicion:fim:passo]
print(tupla[5:9])
```

### Copiado uma tupla para outra

```python
tupla = (1,2,3)
print(tupla)
nova = tupla

outra = (4,5,6)
nova = nova + outra
```

> Na tupla não temos o problema de Shallow Copy

## Porque utilizar tuplas?

- Tuplas são mais rápidas do que listas
-  Tuplas deixam seu código mais seguro
> Isso porque trabalhar com elementos imutáveis traz segurança para o código

