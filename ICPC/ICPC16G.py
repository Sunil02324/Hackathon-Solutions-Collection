def sunil():
	n,m  = map(int,raw_input().split())
	if(m>n):
		return 0
	a = map(int,raw_input().split())
	b = [0]*n
	c = map(int,raw_input().split())
	for p in c:
		b[p] = 1
	count = 0
	for i in range(n):
		p=0
		for j in range(n):
			if(b[j]==1):
				if((a[j]!=1)):
					p= 1
					break
		if p==0:
			count += 1
		x = []
		x.append(b[n-1])
		b = x + b[0:n-1]
	return count

print sunil()