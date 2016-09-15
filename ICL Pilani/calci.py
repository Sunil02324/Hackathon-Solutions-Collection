#t = long(raw_input())

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

# while t>0:
# 	t = t-1
# 	n = long(raw_input())
# 	k = 1
# 	for i in range(1,n+1):
# 		k *= factorial(i)
# 	d = 10**9
# 	d += 7
# 	k %= d 
# 	print k

M=10**9+7
a=[]
a.append(0)
def pCal():
    x=1
    z=1
    i=1
    while i<1000009:
        x=(x%M*i%M)%M
        z=(z%M*x%M)%M
        a.append(z)
        i+=1
pCal()
t=input()
for i in xrange(t):
    n=input()
    print a[n]