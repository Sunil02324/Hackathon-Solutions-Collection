t = int(raw_input())

for i in xrange(t):
	n = int(raw_input())
	a = [int(x) for x in raw_input().split()]
	s = 0
	for j in range(1,n+1):
		if(a[j] > a[0]):
			s += 1
		else:
			continue
	print s