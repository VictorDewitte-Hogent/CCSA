# CLASSIC COMPUTER SCIENCE ALGORITHMS

| Inhoud |
|:---|
|[1. Zoeken en sorteren](#zoeken_en_sorteren)|
|[2. Gelinkte lijsten]()|
|[3. Hashtabellen]()|
|[4. Bomen]()|
|[5. Graafalgoritmes]()|
|[6. Zoekalgoritmes]()|
|[7. Zoeken met een Tegenstander]()|
|[8. Machinaal Leren]()|
|[9. Complexiteitstheorie]()|

### StudieMateriaal

- <a href="https://chamilo.hogent.be/index.php?go=CourseViewer&application=Chamilo%5CApplication%5CWeblcms&course=47756&tool=Document&publication_category=0&browser=Table&tool_action=Viewer&publication=1850076">Cursus in Pdf </a>

- <a href="https://chamilo.hogent.be/index.php?go=CourseViewer&application=Chamilo%5CApplication%5CWeblcms&course=47756&tool=Document&publication_category=271371&browser=Table&tool_action=Browser">Slides in Pdf </a>

- <a href="https://dodona.ugent.be/nl/courses/399/">Dodona oefeningen  </a>

# Zoeken en sorteren

| Inhoud |
|:---|
|[Zoeken in array](#zoeken_in_array)|
|[Linear of sequentieel zoeken](#linear_of_sequentieel_zoeken)|
|[Binair zoeken](#binair_zoeken)|
|[Tijdscomplexiteit]()|
|[Sorteren door selectie]()|
|[Sorteren door tussenvoegen]()|
|[Sorteren door mengen]()|
|[Oefeningen]()|

## Zoeken in array

Zoeken in array
- Klassieke array met elementen
- Effect van gesorteerde array?
- Aanname Array: ophalen elementen in constante tijd onafhankelijk van de positie

<br>


Effect sortering: je hoeft niet meer te zoeken in deel array dat langs de verkeerde kant ligt.

## Linear of sequentieel zoeken
Een array 1 voor 1 overlopen tot je een de gewenste waarde vindt.

<br>

<b>Invoer:</b> Een item `zoekItem` dat moet gevonden worden, een array van items genaamd `rij` met lengte `n`.

<br>

<b>Uitvoer:</b> De index van het eerste element in `rij` dat gelijk is aan `zoekItem`
wordt terug gegeven of `-1` indien `zoekItem` niet voorkomt in `rij`

```bash
function ZoekSequentieel(zoekItem, rij)
    i <- 0                                  #overloopt de posities
    while i < n and rij[i] != zoekItem do   
        i <- i+1
    if i = n then                           #Niet gevonden
        index <- -1
    else                                    #Gevonden
        index <- i
end function
```

<br>

## Binair zoeken
We kunnen ook binair zoeken. Dit werkt enkel in een gesorteerde array.
Zo zoeken we enkel verder in het relevante deel van de array.
- Beschouw een element, bv. het middelste
- Indien het gezochte kleiner is dan het beschouwde: zoek links verder
- Groter: Zoek verder rechts



Merk op dat dit algoritme zowel iteratief als recursief kan werken.<br>
In het geval van recursie
- Basisstap: rij met 1 element
- Recusive stap: alle andere gevallen: Rij wordt gehalveerd

<br>

### Binair zoeken (iteratief)

Rij halveren en verder in de zoeken en opnieuw doen tot dat er 1 element overblijft

<b>Invoer:</b> Een item `zoekItem` dat moet gevonden worden, een <i>gesorteerde</i> array genaamd `rij` van items met lengte `n`<br>
<b>Uitvoer:</b> De index van het eerste element in `rij` dat gelijk is aan `zoekItem` wordt teruggegeven of `-1` indien `zoekItem` niet voorkomt in `rij`
```bash
function ZoekBinair(zoekItem, rij)
    l <- 0
    r <- n-1
    while l != r do         #herhalen todat slechts 1 element overblijft
        m <- [l+r/2] #vloerdeling
        if rij[m] < zoekItem then
            l <- m+1                            #in de rechterhelft zoeken
        else
            r <- m                              #in de linkerhelft zoeken
    if rij[l] = zoekItem then
        index <- l
    else 
        index <- -1
    return index
end function
```
<br>

### Binair zoeken (recursief)

Recursieve stap: de rij wordt gehalveerd.<br>
De functie wordt opnieuw aangeroepen op een deelrij half zo groot asl de oorspronkelijke array.<br>

<b>Invoer:</b> een item `zoekItem` dat moet gevonden worden, een <i>gesorteerde</i> array genaamd `rij` van items van lengte `n`, twee natuurlijke getallen `l` en `r` die het gedeelte van de array aangeven waarin gezocht moet worden.<br>
<b>Uitvoer:</b> de index van het eerste element in `rij` dat gelijk is aan `zoekItem` wordt teruggegeven indien het element voorkomt tussen `rij[l], rij[l+1],...,rij[r]`. De teruggegeven index ligt dan tussen `l` en `r`. Er wordt `-1` teruggegeven indien `zoekItem` niet voorkomt tussen de elementen `rij[l], rij[l+1],...,rij[r]`.
```bash
function zoekRecursief(zoekItem, rij,l,r)
    if l=r then                             # Basisstap, rij van lengte 1
        if zoekItem = rij[l] then
            return l
        else
            return -1
    else
        m <- [l+r/2]#vloerdeling
        if rij[m] < zoekItem then
            return zoekRecursief(zoekItem, rij , m+1 , r) #zoek rechts
        else
            return zoekRecursief(zoekItem, rij , l , m) #zoek links
end function
```     
<br>

### Efficient zoeken

- Binair zoeken is ingewikkelder dan sequentieel zoeken.
- Binair zoeken is beter?
- Focus op 2 zaken:
    1. De uitvoeringstijd
    2. Het geheugengebruik (RAM)

<br>

## Tijdscomplexiteit