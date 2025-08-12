

"""
# paises = { 'br': 'Brasil', 'eua': 'Estados Unidos'}

# print(paises)
# paises2 = dict( br= 'Brasil', eua = 'Estados Unidos', py = 'Paragua

# print(paises['br'])
# print(paises['eua'])
# print(paises['br'])
# print(paises.get('br'))
# print(paises.get('ru'))
# print(paises.get('eua'))
# paises = { 'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}

# print('br' in paises)
# print('ru' in paises)
# print('Brasil' in paises)

# localidades = {
#     #tupla com float               #string
#     (35.123, 39.123): 'Escritório em Tokyo',
#     (40.123, 74.123): 'Escritório em NY',
#     (37.123, 122.123): 'Escritório em São Paulo'
# }

# print(localidades)

# Adicionar elementos
# receita = { 'jan': 100, 'fev': 120, 'mar': 300}
# # forma 1 - mais comum
# receita['abr'] = 350

# print(receita)
# #Forma 2
# novo_dado = {'mai': 500}
# receita.update(novo_dado)

# print(receita)


# receita['mai'] = 1000

# receita.update({'jan': 20 })

# print(receita)

# remover dados de um dicionario
# receita = {'jan': 20, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 1000}

# # forma 1:
# receita.pop('mar')
# print(receita)

# # forma2:
# del receita['fev']
# print(receita)

# Métodos de dic

# d = dict(a=1, b=2, c=3)

# print(d)

# Limpar dicionario

# d.clear()
# print(d)

# Copiando um dicionario para outro

# Forma 1 #deep copy
# novo = d.copy()

# print(novo)
# novo['d'] = 4
# print(d)
# print(novo)

# Forma  2 #shallow copy
# novo = d
# print(novo)
# novo['d'] = 4
# print(d)
# print(novo)

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'numero'], 'desconhecido')

print(usuario)

veja = {}.fromkeys('teste', 'valor')
print(veja)

ex = {}.fromkeys(range(1, 5), 'null')
print(ex)





# Data: 12/08/2025 - Mapas Continuação de dicionários
# Mapas -> Conhecidos em python como dicionários

print(receita)

# Iterando sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f"{chave}: {receita[chave]}")
    
print(receita.keys())

# Modo pythonico - mais recomendado
for chave in receita.keys():
    print(receita[chave])
    

# Acessando valores

print(receita.values())

for valor in receita.values():
    print(valor)
    

# Desempacotamento de dicionários

print(receita.items())

for chave,valor in receita.items():
    print(f"{chave}: {valor}")
    
    
receita = {'jan': 100, 'fev': 250, 'marc': 400}

# Soma* / Valor Max*  / Valor Min* / tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

"""
