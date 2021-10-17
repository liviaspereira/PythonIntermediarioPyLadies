'''Leia um número n e crie uma matriz de ordem n preenchida com números sequenciais de 
1 a n^2.'''

 n = int (input("Digite a ordem da matriz: "))
 matriz = [[i*n +j +1 for j in range(0, n)] for i in range(0,n)]

 print(matriz)