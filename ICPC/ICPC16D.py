t = int(raw_input())
while t>0:
	t = t-1
	n = int(raw_input())
	a = map(int,raw_input().split())
	count = n
	for i in range(0,n):
		for j in range(i+1,n):
			