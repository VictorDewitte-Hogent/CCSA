# <font color=red>CLASSIC COMPUTER SCIENCE ALGORITHMS</font>

| Inhoud |
|:---|
|[1. Zoeken en sorteren](#zoeken-en-sorteren)|
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
|[Zoeken in array](#zoeken-in-array)|
|[Linear of sequentieel zoeken](#linear-of-sequentieel-zoeken)|
|[Binair zoeken](#binair-zoeken)|
|[Tijdscomplexiteit](#Tijdscomplexiteit)|
|[Sorteren door selectie](#Sorteren-door-selectie)|
|[Sorteren door tussenvoegen](#Sorteren-door-tussenvoegen)|
|[Sorteren door mengen](#Sorteren-door-mengen)|
|[Oefeningen](#Oefeningen)|

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

In cursus: focus op uitvoeringstijd. Geen exacte berekening.<br>

Daarom: `Asymptotische analyse` van de uitvoeringstijd. Dit karaktteriseert het gedrag van de uitvoeringstjid voor `grote` waarden van de input. Typisch gedrag is bvb:
- Invoer verdubbelt => uitvoeringstijd verdubbelt
    - Lineaire functie: `T(n) = n`
- Invoer verdubbelt => uitvoeringstijd x4
    - Kwadratische functie; `T(n)= n^2`
- Invoer + 1 => uitvoeringstijd x 2
    - Exponentiele functie: `T(n) = 2^n`
- Invoer verdubbelt => uitvoeringstijd + constante
    - Logaritmische functie: `T(n) = log(n)`
- ...


Bij de analyse van de zoekalgoritmen zien we dat de asymptotischeuitvoeringstijd bepaald wordt door het aantal vergelijkingen dat wordtuitgevoerd.

### Tijdscomplexiteit sequentieel zoeken

Bij sequentieel zoeken kunnen we ons afvragen hoeveel keer de volgende vergelijking wordt uitgevoerd:

`rij[i] != zoekItem`

- Beste geval? => 1
- Slechtste geval? => n
- gemiddelde geval? => n / 2 dus T(n) = 0(n)

We noemen dit lineare tijdscomplexiteit of tijdscomplexi van orde n

### Tijdscomplexiteit binair zoeken

Bij binair zoeken tellen we hoeveel keer de vergelijking

`rij[m] < zoekItem`

Wordt uitgevoerd. Stel: n = 2^k, met `k` een natuurlijk getal.
- n=1, i.e. k=0 => 0 keer
- n=2, i.e. k=1 => 1 keer
- n=4, i.e. k=2 => 2 keer
- n=8, i.e. k=3 => 3 keer

Dus: `n=2^k <=> k = log2(n)`<br>
Dit noemen we logaritmische tijdscomplexiteit: `T(n)=0(log2(n))`<br>

## Sorteren door Selectie

Basisidee:
- Zoek het grootste element en plaats het achteraan
- Sorteer de rest van de array

<b>Invoer:</b> De array `a` is ingevuld met `n` elementen.
<b>Uitvoer:</b> De array `a` is gesorteerd.
```bash
function selectionSort(a)
    for i = n-1...1 by -1 do            # achteraan starten
        positie <- i
        max <- a[i]
        for j = i -1 ... 0 by -1 do     # j doorloopt de deelrij
            if a[j] > max then
                positie <- j
                max <- a[j]
        a[positie] <- a[i]          # grootste element wisselen met laatste
        a[i] <- max
end function
```
Voorbeeld:

<img src="img\SorterenDoorSelectie.png" width=400>

### Complexiteitsanalyse

De uitvoeringstijd wordt bepaald door het aantal keer dat de vergelijking `a[j] > max` op regel 6 uitgevoerd wordt, of het aantal keer dat de teller j wijzigt.

<img src="img\ComplexiteitsanalyseSorterenSelectie.png" width=400>

We besluiten : `T(n)= 0(n^2)`

### Hoe werd die som bepaald?

Voorbeeld: bereken: 1 + 2 + 3 +...+ 10.
| Stijgend  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
|-----------|----|----|----|----|----|----|----|----|----|----|
| Omgekeerd | 10 | 9  | 8  | 7  | 6  | 5  | 4  | 3  | 2  | 1  |
| Som       | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 |

Dus:            1+2+3+...+10 = (11*10)/2
<br>
Algemeen:       1+2+3+...+m = ((m+1)m)/2


## Sorteren door tussenvoegen

Basisidee:
1. Veronderstel dat er reeds een deel vooraan de array gesorteerd is.
2. Neem het eerste element van het niet gesorteerde deel en voeg ditelement toe op de juiste plaats in het gesorteerde deel. Op dezemanier wordt het gesorteerde deel uitgebreid.

Sorteren door tussenvoegen of “card sort“ kan m.a.w. het bestvergeleken worden met het op volgorde steken van kaarten.<br>

<img src="img\SorterenDoorTussenVoegen.png" width=400>

<b>Invoer:</b> De array `a` is gevuld met `n` elementen.
<b>Uitvoer:</b> De array `a` is gesorteerd.

```bash
function cardSort(a)
    for i= 1...n-1 do
        x <- a[i]               # x bevat het ini te voegen element
        j <- i                      # j zoekt de juiste positie voor x
        while j>0 and x<a[j-1] do   # schuif grotere elementen op
            a[j] <- a[j-1]          # schuif a[j-1] eentje op
            j <- j-1
        a[j] <- x               # x wordt op de juiste positie tussengevoegd
end function
```

### Complexiteitsanalyse

Kwadratische tijdscomplexiteit,

## Sorteren door mengen

Sorteren door mengen (mergesort) is een ingewikkelder algoritme dan de voorgaande twee eenvoudige sorteeralgorimtes maar is ook een heel stuk efficienter. <br>

Basisidee:
1. Sorteer de eerste helft van de array.
2. Sorteer de tweede helft van de array.
3. Meng de twee gesorteerde deelrijen samen tot 1 gesorteerde array.

De eerste twee stappen in dit proces gebeuren op eenrecursievemanier. Merk op dat het eigenlijk sorteren gebeurt bij het mengen vande twee gesorteerde rijen.

Voorbeeld:<br>
<img src="img\SorterenDoorMengen.png" width=400><br>
<img src="img\SorterenDoorMengen2.png" width=400>

De functie `mergeSort` roept de recursieve functie `mergeSortRecursive` aan. In deze methode wordt een deel van de rij gesorteerd door het te sortern deel op te splitsen in twee deelrijen van halve lengte.<br>
Vervolgens worden de gesorteerde deelrijen gemengd. Het samenvoegen van de beide deelrijen gebeurt in de functie `merge`.

<b>Invoer:</b> De array `a` is gevuld met `n` elementen. <br>
<b>Uitvoer:</b> De array `a` is gesorteerd.
```bash
function mergeSort(a)
    mergeSortRecursive(a,0,n -1)
end function
```

<b>Invoer:</b> De array `a` is gevuld met `n` elementen, begin en einde wijzen naar geldige posities in de array `a`. <br>
<b>Uitvoer:</b> De elementen met index `begin` tot en met index `einde` werden gesorteerd.
```bash
function mergeSortRecursive(a, begin, einde)
    if begin < einde then
        midden <- [(begin + einde)/2] #vloerdeling
        mergeSortRecursive(a,begin,midden)
        mergeSortRecursive(a, midden+1,einde)
        merge(a,begin,midden,einde)
end function
```

### De functie merge

<b>Invoer:</b> De array𝑎is gevuld met𝑛elementen; de elementen van dedeelrij gaande van debegin-positie tot en met demidden-positie zijngesorteerd; de elementen van de deelrij gaande van de(midden+1)-positie tot en met deeind-positie zijn gesorteerd.<br>
<b>Uitvoer:</b> De elementen met indexbegint.e.m. indexeindewerdengesorteerd.

```bash
function Merge(a,begin,midden,einde)
    j<- begin                                           # De teller i doorloopt de linkse deelrij
    j<- midden+1                                        # De teller j doorloopt de rechtse deelrij
    k<- i                                               # De teller k doorloopt de hulparray hulpa
    hulpa <- nieuwe array[n]                            # tijdelijke hulpopslag
    while i <= midden and j <= einde do                 # totdat een deelrij leeg is
        if a[i] <= a[j] then                            # Het kleinste element komt eerst
            hulpa[k] <- a[i] ; i <- i + 1
        else
            hulpa[k] <- a[i] ; j <- j + 1
        k <- k +1
    if i>midden then
        while j<= einde do
            hulpa[k] <- a[j] ; j <- j + 1 ; k <- k+1
    else
        while i <= midden do
            hulpa[k] <- a[i] ; i <- i + 1 ; k <- k+1
    for k = begin...einde do
        a[k] <- hulpa[k]
end function
```

### Complexiteitsanalyse

### Geheugengebruik

- Mergesort is dus tijdsefficienter dan voorgaande.
- doch minder geheugen efficient.
- `Merge`-algoritme: extra hulprij nodig.

## Oefeningen
... zie dodona enzo

# Gelinkte lijsten

| Inhoud ||
|:---|:---|
|[Gelinkte lijsten](#Gelinkte-lijsten)||
||[Specificatie](#Definitie)|
||[Gelinkte lijst]()|
||[Ankercomponenten]()|
||[Dubbelgelinkte lijsten]()|
|[Stapels](#Stapels)|
||[Specificatie]()|
||[Toepassingen van Stapels]()|

## Inleiding

- Array = eenvoudige datastructuur.
- Maar wat met elementen tussenvoegen? Of verwijderen in het midden?
- Bewerkingen hebben lineaire tijdscomplexiteit.
- Oplossing? Gelinkte lijsten.
- Toevoegen of verwjderen in constante tijd.
- Opzoeken van een element bljft echter een lineare tijdscomplexiteit vertonen.
- Nog een voordeel: aantal elementen toevoegen kan onbeperkt, geen limieten op de grootte zoals bij array.

## Definitie

Een gelinkte lijst bestaat uit een aantalknopendie via eenkettingstructuuraan elkaar geschakeld zijn. Een knoop bestaat uit tweevelden:
- Een data-veld `data`
- Een veld `volgende`
De laatste knoop bevat een wijzernull: dit wordt grafisch voorgestelddoor een schuine streep.<br>
Voor de eerste knoop moet een referentieeerstebijgehouden worden.In een lege lijst is de referentieeerstegelijk aan null.

### Een enkelvoudige geschakelde lijst

<img src="img\EnkelvoudigGeschakeldeLijst.png" width=400>

### Basisbewerkingen

De belangrijkste basisbewerkingen voor een enkelvoudige geschakelde lijst zijn:
- zoek(): zoekt de positie van de knoop met als data-veld het argument.
- verwijder(): verwijdert de knoop die volgt na de opgegeven knoop en geeft de waarde van het data-veld van de verwijderde knoop weer.
- voegToe(): voegt een knoop toe na een opgegeven knoop, het data-veld krijgt de waarde van het tweede argument.

### Klasse knoop in uml

<img src="img\knoopInUml.png">

De gedefinieerde knoop is een datastructuur die een element van een niet nader gedefinieerde klasse Element bevat.

### Constructor van Knoop
De constructor maakt nieuw object van klasse knoop aan.

<b>Invoer:</b> / 
<b>Uitvoer:</b> Er werd een nieuwe knoop aangemaakt.

```bash
function Knoop
    data <- null
    volgende <- null
end function
```

### Implementatie Gelinte Lijst

<br>

### Algoritme voor de constructor

De constructor GelinkteLijst maakt een nieuw object van de klasse GelinkteLijst aan.

<b>Invoer:</b> / 
<b>Uitvoer:</b> er werd een nieuwe (lege) gelinkte lijst aangemaakt.
```bash
function GelinkteLijst
    eerste <- null
end function
```

### Opzoeken van een element x

<b>Invoer:</b> De gelinkte lijst werd aangemaakt,𝑥is het te zoeken element.
<b>Uitvoer:</b> De referentie naar de eerste knoop met dataveld gelijk aan𝑥werd geretourneerd, indien𝑥niet voorkomt in de lijst werd dereferentie null geretourneerd.
```bash
function zoek(x)
    ref <- eerste
    while ref != null and ref.data != x do
        ref <- ref.volgende
    return ref
end function
```

### Tijdscomplexiteit van `zoek`
