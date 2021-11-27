


notenTypes = {
  '': [0,4,7] ,
  'm' : [0,3,7],
  '7':[0,4,7,10],
  'm7' : [0,3,7,10],
  'M7': [0,4,7,11]
}
noten_= ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notenRepeat = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notenHashtag= ["C#","D#",'F#', "G#", "A#"]
def ontleding(a):
    
    if "#" in a:
        for i in notenHashtag:
            if i in a:
                if len(i) == 2:
                    b1 = slice(0,2)
                    b2 = slice(2, len(a))
               
    else:
        for i in noten_:
            if i in a:
                if len(i) == 2:
                    b1 = slice(0,len(a)//2)
                    b2 = slice(len(a)//2, len(a))
                else:
                    b1 = slice(0,1)
                    b2 = slice(1, len(a))
    return a[b1],a[b2]

def noten(a,b):
    iOne =b[0]
    iTwo = b[1]
    iThree = b[2]
    try:
        iFour= b[4]
    except IndexError:
        iFour = 0
    
    indexA=0
    for i in notenRepeat:
        if i in a:
            indexA = i
    output = [a,notenRepeat[indexA+iOne], notenRepeat[indexA+iTwo],notenRepeat[indexA+iThree]]
    if iFour !=0:
        output = [a,notenRepeat[indexA+iOne], notenRepeat[indexA+iTwo],notenRepeat[indexA+iThree], notenRepeat[indexA+iFour]]
    return output
               

