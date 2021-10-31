idades = [12, 23, 34, 45, 56, 67, 78, 89]
print("Com função")
def quadrado(x):
  return x ** 2

for idade in idades:
  print(quadrado(idade))


print("\nCom função anônima")

idades_filtradas = map(lambda x: x**2, idades)

print("\n".join(map(str, idades_filtradas)))
