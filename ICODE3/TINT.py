n = int(raw_input())
a = []
while n>0:
	p,q = map(int, raw_input().split())
	c = max(p,q)
	a.append(c**2)
	n = n-1
d = sum(a)
e = int(d**(.5))
print e