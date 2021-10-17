'''Leia 10 números separados por espaços, e crie um dicionário associando cada número com seu 
quadrado, se o quadrado for menor que 100.'''

lista = map(int, input("Digite 10 numeros? ").split())

dicionario = {elemento: elemento**2 for elemento in lista if elemento**2 <100}

print(dicionario)
