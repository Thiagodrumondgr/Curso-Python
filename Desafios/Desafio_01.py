nome =input("Digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("Digite seu peso: "))
ano_atual = 2024

ano_nascimiento = ano_atual - idade
imc = peso / altura** 2

print(f"{nome} tem {idade} anos sua altura é {altura} seu peso atual é {peso} e nasceu no ano de {ano_nascimiento}")
print(f"Seu IMC é de {imc:.2f}")