# Diferença entre Dct e Ordered Dict

#Dict

dict1 = { 'a': 1, 'b': 2} 
dict2 = { 'b': 2, 'a': 1} 

print(dict1 == dict2)
# São iguais porque a ordem não importa 

# Ordered Dict
from collections import OrderedDict
odict1 = OrderedDict({ 'a': 1, 'b': 2}) 
odict2 = OrderedDict({ 'b': 2, 'a': 1} )

print(odict1 == odict2)