t = int(raw_input())
while t>0:
	t = t-1
	k,l,e = map(int, raw_input().split())
	s = e
	a = []
	a = map(int,raw_input().split())
	b = sum(a)
	#print b
	s += b
	#print s%l
	if s%l == 0:
		print "YES"
	else:
		print "NO"
