t = int(raw_input())
while (t>0):
	t = t -1
	n,m = map(int, raw_input().split())
	a = []
	b = []
	for i in range(0,m):
		x,y = map(int, raw_input().split())
		a.append(x)
		b.append(y)
	