'''Criação de um dicionário normal (sem comprehensions)'''

frase = input("Digite uma frase")
dicionario = {}

for pos, palavra in enumerate(frase.split()):
  dicionario[pos] = palavra

print(dicionario)