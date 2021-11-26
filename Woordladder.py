#https://dodona.ugent.be/nl/courses/399/series/8799/activities/1200279845/
def precies_een_verschillend(woord1,woord2):
    if(len(woord1) != len(woord2)):
        return False
    aantalVerschil = 0
    for i,letter in enumerate(woord1):
        if woord1[i] != woord2[i]:
            aantalVerschil += 1
    return aantalVerschil == 1

def maak_graaf(woordenArr):
    dict = {woord1 : set() for woord1 in woordenArr}
    for i, woord1 in enumerate(woordenArr):
        for j in range(i+1,len(woordenArr)):
            woord2 = woordenArr[j]
            if precies_een_verschillend(woord1,woord2):
                dict[woord1].add(woord2)
                dict[woord2].add(woord1)
    return dict