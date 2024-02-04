estagiario1 = input("Nome estagiagio: ")
salario1 = float(input("Qual seu salario atual? "))
experiencia1 = int(input("Quanto tempo de experiencia na area? "))

estagiario2 = input("Nome estagiagio: ")
salario2 = float(input("Qual seu salario atual? "))
experiencia2 = int(input("Quantos anos de experiencia na area? "))

if salario1 > salario2:
    maior_salario = estagiario1
else:
    maior_salario = estagiario2
    
if experiencia1 > experiencia2:
    maior_experiencia = estagiario1
else:
    maior_experiencia = estagiario2
print("##########################################")
print("EXPERIENCIA ESTAGIARIO 1")
print("##########################################")
print (f"Nome do estagiario1 : {estagiario1}")
print(f"Salario estagiario1 :{salario1:.2f}")
print(f"Tempo de experiencia estagiario1 : {experiencia1} anos")

print("##########################################")
print("EXPERIENCIA ESTAGIARIO 2")
print("##########################################")

print (f"Nome do estagiario2 : {estagiario2}")
print(f"Salario estagiario2 {salario2:.2f}")
print(f"Tempo de experiencia estagiario2 : {experiencia2} anos")

print("##########################################")

print (f"O funcionario com maior salario é o {maior_salario}, e o estagiario com maior tempo de experiencia é o {maior_experiencia}")
