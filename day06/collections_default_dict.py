# dicionario = {'nome': 'Gabrielle'}

# print(dicionario)
# print(dicionario['nome'])
# print(dicionario['sobrenome']) #KeyError


from collections import defaultdict

dicionario = defaultdict(lambda:1)

dicionario['curso'] = 'Geek'
print(dicionario)

print(dicionario['outro'])
print(dicionario)
