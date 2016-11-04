t = int(raw_input())
while t>0:
	t = t-1
	s,v = map(int, raw_input().split())
	ans = float(2*s)/float(3*v)
	print '{0:.6f}'.format(ans)