totaal = 0
checker = False
while checker == False:
    
    kaart = int(input())
    totaal+= kaart
    if totaal==21:
        print("Gewonnen!")
        checker = True
    if totaal > 21:
        print(f"Verbrand ({totaal})")
        checker = True
    if kaart == 0:
        print(f"Voorzichtig gespeeld ({totaal})")
        checker = True
    



    