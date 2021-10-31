import pandas as pd

entrada = pd.read_csv("entrada.csv")
print(entrada)
entrada["email"] = entrada["nome"].apply(lambda nome: nome.lower().split()[0] + "@pyladies.com")
# senha_contem letras e numeros 
entrada["senha"] = entrada["chars"].apply(lambda char: "".join([x for x in char  if x.isalnum()]))

# divisão inteira de num2 por num1

entrada["divisao"] = entrada.apply(lambda x: x.num2//x.num1 , axis=1)

print(entrada["divisao"])