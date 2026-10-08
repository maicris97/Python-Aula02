#1 - Crie uma lista com 5 filmes favoritos, mostre o primeiro, o último e o total.
#2 - Peça 5 números, guarde em uma lista e mostre o maior, o menor e a soma(max,min,sum)
#3 - Crie um dicionário com os dados de um celular(marca,modelo,preço) e mostre cada par chave-valor com for chave, valor in dicionario.item()

#1:
filmes=["Pânico","Antes do Amanhacer","A Viagem de Chihiro","O Exorcista","Brilho Eterno de Uma Mente Sem Lembranças"]
print(filmes[0])
print(filmes[-1])
print(len(filmes))

#2:
numeros = []
for i in range(5):
    numeros.append(int(input(f"Número {i + 1}: ")))
print(f"Maior: {max(numeros)} | Menor: {min(numeros)} | Soma: {sum(numeros)}")
