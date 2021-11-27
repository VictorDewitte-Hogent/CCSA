h = int(input())
b = int(input())
x = 0
y = 0
coords = (x,y)
pockets = ((0, 0), (0, h), (b, h), (b, 0))
while ( coords in pockets == False):
    while True:
        x+=1
        y+=1
        if y == h:
            print(f"top cusshion ({x},{y})")
            break
    while True:
        x+=1
        y-=1
        if x == b:
            print(f"right cushion ({x},{y})")
            break
    while True:
        x-=1
        y-=1
        if y == 0:
            print(f"bottem cushion ({x},{y})")
            break
    while True:
        x-=1
        y+=1
        if x == 0:
            print(f"left cusshion ({x},{y})")
            break
print(coords)z