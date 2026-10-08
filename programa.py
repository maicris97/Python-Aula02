# nome = "Maiara"
# idade = 28
# altura = 1.57
# print(f'Meu nome é {nome}, tenho {idade} anos e minha altura é de {altura}m.')

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso= float(input("Digite seu peso: "))
imc = peso / altura ** 2
print(f'Meu nome é {nome}, tenho {idade} anos, minha altura é de {altura}m, meu peso é de {peso}kg e meu IMC é de {imc:.2f}.')
