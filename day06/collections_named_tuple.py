# Collections -  Named Tuple

from collections import namedtuple

#Forma 1 - Declaração
cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2  - Declaração

cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3 -  Declaração
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca= 'Chow-CHow', nome='Ray')
jose = cachorro3(6, 'Vira Lata', 'Jose')
print(ray)
print(jose)

# Acessando os dados

# Forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print(jose.idade)
print(jose.raca)
print(jose.nome)
