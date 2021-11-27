a = int(input())
b = int(input())

som_a= 0
for i in range(1,a):
    if a%i == 0:
        som_a += i

som_b = 0
for i in range(1,b):
    if b%i == 0:
        som_b += i

if som_a == b and som_b == a:
    print(f"{a} en {b} zijn bevriende getallen")
else:
    print(f"{a} en {b} zijn geen bevriende getallen")