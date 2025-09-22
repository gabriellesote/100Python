from collections import Counter

# nome = 'gabrielle soares'
# contador = Counter(nome)
# print(contador)

# lista = ["peixe", "peixe", "macarrão", "feijão", "feijão"]
# print(Counter(lista))

texto = """ By submitting this form, I agree that JetBrains s.r.o. 
may process the personal data I provided above and my 
location for the purpose explained above and may engage third parties 
in such processing. The consent can be revoked in my profile at any time.
 More details about the processing are in JetBrains Privacy Notice. 
In addition, an unsubscribe link is included in each email."""


palavras = texto.split()

contar = Counter(palavras)
print(contar.most_common(2))