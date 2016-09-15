def LeastPrimeDivisor(n):
    i = 2
    while i<=n:
        print i
        if(n%i==0):
            break
        i=i+1
    return i

def findSmallestFactor(n):
    res 
    factor = 2 
    while factor < n and n % factor != 0: 
        factor += 1
    return factor

def Update(a,L,R):
	for k in range(L,R+1):
		a[k-1] = a[k-1]/LeastPrimeDivisor(a[k-1])

def Get(a,l,r):
    s = int(1)
    j = l
    while j < r+1:
        s = max(s,LeastPrimeDivisor(a[j-1]))
    return s


T = int(raw_input())
while T > 0:
    T = T - 1
    n,m = map(int,raw_input().split())
    a = map(int,raw_input().split())
    output = ''
    for o in range(0,m):
        k, L, R = map(int,raw_input().split())
        if k==0:
            Update(a,L,R)
        else:
            output += str(Get(a, L,R)) + " "
    print output
