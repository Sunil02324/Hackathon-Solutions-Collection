t = int(raw_input())
while (t>0):
	t = t -1
	m,n,x,y,d = map(int, raw_input().split())
	a = [[]]*m
	for i in range(0,m):
		b = raw_input().spit()
		a[i] = b
	count = 0
	p = 0
	q = 0
	
	if count > 0:
		print count
	else:
		print -1
