import math
x1 = float(input("Informe o primeiro valor: "))
x2 = float(input("Informe o segundo valor: "))
y1 = float(input("Informe o terceiro valor: "))
y2 = float(input("Informe o quarto valor: "))
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"{dist:.4f}")