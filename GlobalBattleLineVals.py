from copy import deepcopy

global sortedhands
global handvaldict

hands={}

for x in range(60):
    for y in range(x+1,60):
        for z in range(y+1,60):
            hands[(x,y,z)] = x%10 + y%10 + z%10


            
for x in range(6):
    for y in range(x,6):
        for z in range(y,6):
            for w in range(8):
                hands[(10*x + w, 10*y+w+1, 10*z+w+2)] = 60 + w
                hands[(10*x + w+2, 10*y+w+1, 10*z+w)] = 60 + w
                hands[(10*x + w+1, 10*y+w+2, 10*z+w)] = 60 + w
                hands[(10*x + w, 10*y+w+2, 10*z+w+1)] = 60 + w
                hands[(10*x + w+2, 10*y+w, 10*z+w+1)] = 60 + w
                hands[(10*x + w+1, 10*y+w, 10*z+w+2)] = 60 + w


for x in range(10):
    for y in range(x+1,10):
        for z in range(y+1,10):
            for w in range(6):
                hands[(x+10*w,y+10*w,z+10*w)] = x+y+z + 80
                


for x in range(6):
    for y in range(x+1,6):
        for z in range(y+1,6):
            for w in range(10):
                hands[(10*x+w,10*y+w,10*z+w)] = 150 + w


for y in range(60):
    z = y % 10 
    if z <= 7:
        hands[(y,y+1,y+2)] = 200 + z



def mergeSort(alist,d):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,d)
        mergeSort(righthalf,d)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if d[lefthalf[i]] > d[righthalf[j]]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return(alist)

listofhands = []

for x in hands:
    listofhands += [x]

sortedhands = mergeSort(listofhands,hands)

handvaldict = listofhands
