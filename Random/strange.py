t = int(raw_input())

for i in xrange(t):
	n,x,m = map(int,raw_input().split())
	a = raw_input().split()
	for j in range(0,m):
		for k in range(1,n):
			a[k] = int(a[k]) + int(a[k-1])
	c = int(a[x-1])
	s = 10**9
	s += 7
	c %= s
	print int(c)