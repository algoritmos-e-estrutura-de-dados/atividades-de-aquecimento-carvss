import math
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))
tri = (a * c)/2
cir = math.pi * c**2
tra = ((a + b)/2)*c
qua = b * b
ret = a * b
print(f"TRIÂNGULO: {tri:.3f}")
print(f"CÍRCULO: {cir:.3f}")
print(f"TRAPÉZIO: {tra:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETÂNGULO: {ret:.3f}")