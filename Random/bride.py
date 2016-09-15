t = int(raw_input())
l = []
def kill(l):
	b = l[1]
	#print b
	l.pop(0)
	#print l
	l.pop(0)
	#print l
	l.append(str(b))
	#print l
	return l

for i in range(0,t):
	n = int(raw_input())
	l = list(range(1,n+1))
	for j in range(0,n-1):
		l = kill(l)
	print l[0]