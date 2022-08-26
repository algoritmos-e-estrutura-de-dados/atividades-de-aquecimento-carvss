a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))
c = int(input("Informe o terceiro valor: "))
m = (a + b + abs(a - b))/2
maior = (m + c + abs(m - c))/2
print(maior, "é o maior")