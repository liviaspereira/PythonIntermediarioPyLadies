'''geradores só faz quando você mandar é usado para muitos dados, é chamado de preguiçosa, nunca 
faz nada previamente.'''

x = 100

def geradores(y):
  for i in range(y):
    yield i**2

gen_comp = (i for i in geradores(x))
print(gen_comp)


comp = [i**2 for i in range(x)]

print(comp)
