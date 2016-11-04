from math import sqrt
t = int(raw_input())
while t>0:
	t = t-1
	n,m,c = map(int, raw_input().split())
	count = 0
	z = 2 if c%2 else 1
	fac = set(reduce(list.__add__, ([i] for i in range(1, int(sqrt(c))+1, z) if c % i == 0)))
	for j in fac:
		w = j
		h = c/j
		if h <= n and w <= m:
			if h == w:
				count += 1
				continue
			if w <= n and h <= m:
				count += 2
			else:
				count += 1
		elif h <= m and w <= n:
			if h == w:
				count += 1
				continue
			if w <= m and h <= n:
				count += 2
			else:
				count += 1
	print count	