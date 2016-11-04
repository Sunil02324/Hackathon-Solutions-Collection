t = int(raw_input())
while (t>0):
	t = t -1
	n = int(raw_input())
	a = map(int,raw_input().split())
	arith = True
	number = 0
	d = []
	if n == 2:
		print min(a)
	else:
		for i in range(1,n):
			d.append(a[i] - a[i-1])
		
		print d
		