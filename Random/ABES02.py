t = int(raw_input())
while t>0:
	t = t-1
	n = int(raw_input())
	a = map(int,raw_input().split())
	a.sort()
	b = []
	c = []
	if n%2 == 0:
		for i in range(0,n/2):
			b.append(a[i])
		for i in range(n/2,n):
			c.append(a[i])
	else:
		for i in range(0,(n-1)/2):
			b.append(a[i])
		for i in range((n-1)/2, n):
			c.append(a[i])
	b.sort()
	c.sort(reverse = True)
	for i in range(0,n,2):
		a[i] = b[0]
		b.pop(0)
	for i in range(1,n,2):
		a[i] = c[0]
		c.pop(0)
	for x in a:
		print x,
	print