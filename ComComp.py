'''Criação de um dicionário com comprehensions'''

frase = input("Digite uma frase")

dicionario = {pos: palavra for pos, palavra in enumerate(frase.split())}

print(dicionario)