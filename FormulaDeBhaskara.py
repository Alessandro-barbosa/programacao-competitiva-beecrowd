a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
delta = (b ** 2) - (4 * a * c)
if delta < 0 or a == 0:
    print("Impossivel calcular")
    exit()
x_um = (-b + delta ** (1 / 2)) / (2 * a)
x_dois = (-b - delta ** (1 / 2)) / (2 * a)
print(f"R1 = {x_um:.5f}")
print(f"R2 = {x_dois:.5f}")