piraten = int(input())
noten = int(input())

for i in range(1, piraten+1):
    gestolenNoten = noten // piraten
    notenAap = noten % piraten
    
    
    if notenAap > 1:
        string = f'{notenAap} noten'
    elif notenAap == 1:
        string = f'{notenAap} noot'
    else : 
        string = 'geen noten'
    
    print(f'{int(noten)} noten = {gestolenNoten} noten voor piraat#{i} en {string} voor de aap')
    noten = noten - gestolenNoten - notenAap
    if i == piraten:
        geslotenNoten = noten // piraten
        notenAap =  noten % piraten
        
        if notenAap > 1:
            string = f'{notenAap} noten'
        elif notenAap ==1:
            string = f'{notenAap} noot'
        else: 
            string = 'geen noten'
        print(f'elke piraat krijgt {gestolenNoten} noten en {string} voor de aap')