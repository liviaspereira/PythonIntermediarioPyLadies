'''lambda usado para coisas simples'''

idades = [12, 23, 34, 45, 56, 67, 78, 89]
print("Com função")
def maior_de_idade(x):
  if x > 18:
    return f"{x} é maior de idade"
  return f"{x} é menor de idade"

for idade in idades:
  print(maior_de_idade(idade))


print("\nCom função anônima")
maior_de_idade2 = lambda x: f"{x} é menor de idade" if x < 18 else f"{x} é maior de idade"

idades_filtradas = map(maior_de_idade2, idades)

print("\n".join(idades_filtradas))