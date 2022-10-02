n = float(input("Informe o número do funcionario:"))
wh = float(input("Informe o número de horas trabalhadas no mês:"))
ph = float(input("Informe o valor recebido por hora de trabalho:"))
salary = wh * ph
print(f"NUMBER = {n:.0f}")
print(f"SALARY = U$ {salary:.2f}")