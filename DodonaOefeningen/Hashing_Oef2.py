def twoSum(a,t):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j]==t:
                return[i,j]
    return None
    
def twoSumHash(a,t):
    dict={}
    n = len(a)
    for i in range(n):
        aj = t-a[i]
        if aj in dict:
            j = dict[aj]
            #return [min(i,j), max(i,j)]
            return [j,i]
        else:
            dict[a[i]]=i
    return None