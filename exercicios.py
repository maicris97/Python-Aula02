# 1 - Peça o nome e a idade  e mostre: "_________, daqui há 10 anos você terá _______ anos."
# 2 - Peça uma temperatura em Celsius e converta para Fahrenheit(F= C * 9/5 + 32)
# 3 - Peça a base e a altura de um retângulo e mostre a área e o perímetro.
# 4 - Peça 3 notas e mostre a média.
# 5 - Refaça a calculadora IMC, colocando o seguinte:
# Abaixo de 18,5: Abaixo do peso
# 18,6 a 24,9: Peso normal ou ideal
# 25 a 29,9: Sobrepeso
# 30 a 34,9: Obesidade grau I
# 35 a 39,9: Obesidade grau II (severa)
# Acima de 40: Obesidade grau III (mórbida)

#1:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
idade10anos = idade + 10
print(f"Seu nome é {nome} e você tem {idade} anos, daqui a 10 anos você terá {idade10anos} anos.")

print()
#2:
celsius = float(input("Digite a temperatura em celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"A temperatura em celsius é de {celsius}, convertida para fahrenheit fica {fahrenheit}F")

print()
#3:
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
perimetro = (base + altura) * 2
print(f"A área do retângulo é {area:.2f} e o perímetro é {perimetro:.2f}")

print()
#4:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das três notas é {media:.2f}")

print()
#5:
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura ** 2

if imc <= 18.5:
    print(f"Abaixo do peso")
elif imc > 18.6 and imc <=24.9:
    print(f"Peso normal ou ideal")
elif imc > 25.0 and imc <= 29.9:
    print(f"Sobrepeso")
elif imc > 30.0 and imc <= 34.9:
    print(f"Obesidade grau I")
elif imc > 35.0 and imc <= 39.9:
    print(f"Obesidade grau II(severa)")
else:
    print(f"Obesidade grau III(mórbida)")

print()
print(f"Meu nome é {nome}, minha altura é {altura:.2f}cm, meu peso é {peso:.2f}kg e meu IMC é de {imc:.2f}")

