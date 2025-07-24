
## END

Em Python, a palavra-chave `end` é usada com a função `print()` para especificar o caractere ou string que será adicionado ao final da saída. Por padrão, `print()` adiciona uma quebra de linha (`\n`) ao final de cada chamada. Utilizando o parâmetro `end`, é possível alterar esse comportamento, por exemplo, para imprimir vários valores em uma mesma linha ou adicionar outros caracteres no final da saída. 

Como usar o parâmetro `end`:

O parâmetro `end` é um argumento nomeado da função `print()`. Ele recebe uma string como valor, que será adicionada ao final da saída do `print`.

```python
print("Olá", end=" ")
print("Mundo!")
# Saída: Olá Mundo!
```


## Contagem em Python 

> **Não existe `++` nem `--` em Python**. Isso é algo que vem de linguagens como C, Java, JavaScript etc.

No Python, **`+=` é uma instrução** (uma operação de atribuição), **não pode estar dentro de `print()`**.


## Descarte de valor Python

 Dica python: colocar um underline em uma variável que não irá precisar, faz com que o python descarte essa variável. Exemplo: 

```python
nome = "Gabrielle"
for _,v in enumerate(nome):
	print(i, v)
```

Como o enumerate retorna 2 valores, desse jeito com o underline, esse valor será descartado. 


## Sobre Strings

No python tem como concatenar strings

```python
nome = "Gabrielle"
nome + " Soares"

#output:
Gabrielle Soares
```

Tem como multiplicar strings:

```python
nome = "gabi"
nome * 3
# output:
gabigabigabi
```


# Múltiplos inputs

## Usando input() com split()

Uma das maneiras mais simples de tomar várias entradas de um usuário em Python é usando a função input() junto com o método split(). O método split() divide uma string em uma lista com base em um separador especificado (por padrão, usa espaço em branco).

```python
# taking two inputs at a time
x, y, z = input("Values: ").split()
print(x)
print(y)
print(z)
```
Como funciona:

- input() toma a entrada completa como uma única string.
- .split() divide a cadeia em componentes separados com base em espaço em branco por padrão.
- Os valores são atribuídos a variáveis individuais (x, y, z).

