arr = int(input())
def printAl(arr):
    
    a = []
    for i in range(arr):
        c = a.append(i)
    return(a[1:arr:2])
        
        
c = printAl(arr)
for j in c:
    print(j,end =" ")

        