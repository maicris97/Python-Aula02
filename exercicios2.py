#1 - MOSTRE A TABUADA DE UM NÚMERO ESCOLHIDO PELO USUÁRIO(1 A 10)
#2 - SOME TODOS OS NÚMEROS DE 1 A 100 USANDO FOR
#3 - FAÇA UMA CONTAGEM REGRESSIVA DE 10 ATÉ 1 E NO FIM MOSTRE "FOGO!"
#4 - PEÇA UMA SENHA REPETIDAMENTE ATÉ O USUÁRIO DIGITAR "python123"

#1:
# numero = int(input("Tabuada do número: "))

# for tabuada in range(1, 11):
#     print(f"{numero} X {tabuada} = {numero * tabuada}")

#2:
# soma=0

# for i in range(1, 101):
#     soma+=i
# print(soma)

#3:

# for i in range(10, 0, -1):
#     print(i)
# print("FOGO!") 

#4:
senha =' '

while senha != "python123":
    senha = input("Digite a senha correta: ")
print("Acesso liberado!")
       

