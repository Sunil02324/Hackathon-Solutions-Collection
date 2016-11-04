t = int(raw_input())
while t>0:
	t = t-1
	n = int(raw_input())
	a=[[]]*n
	invi = True
	for i in range(0,n):
		a[i] = map(int,raw_input().split())
	x = -1
	y = -1
	for i in range(0,n):
		for j in range(0,n):
			if a[i][j] == 5:
				x = i
				y = j
				break
	if x == -1:
		print x
	else:
		dist = 0
		for i in range(0,n):
			for j in range(0,n):
				if a[i][j]==1:
					dist += abs(x-i) + abs(y-j)
		print dist
