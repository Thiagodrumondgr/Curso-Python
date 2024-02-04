funcionario1 = input("Digite o nome do funcionario: ")
salario1 = float(input("Digite seu salario: "))
funcionario2 = input("Digite o nome do funcionario: ")
salario2 = float(input("Digite seu salario: "))
if salario1 >= salario2:
    maior_salario = funcionario1
else:
    maior_salario = funcionario2

print (f"O nome do funcionario 1 é {funcionario1}")
print(f"O salario do funcionario 1 é de {salario1:.2f}")

print (f"O nome do funcionario 2 é {funcionario2}")
print(f"O salario do funcionario 2 é de {salario2:.2f}")
print(f"O Funcionario que tem o maior salario é o {maior_salario}")
