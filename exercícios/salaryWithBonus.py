n = input("Informe o nome do vendedor:")
sf = float(input("Informe o salário fixo do vendedor:"))
ts = float(input("Informe o valor total vendido pelo vendedor no mês:"))
bonus = (ts * 15)/100
salary = sf + bonus
print(f"TOTAL = R$, {salary: .2f}")