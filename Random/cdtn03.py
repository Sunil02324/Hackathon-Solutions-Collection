n,m,q = map(int,raw_input().split())
a = [[]]*n
intact = 0
for i in range(0,n):
	a[i] = map(int,raw_input().split())
	for j in a[i]:
		if j == 1:
			intact += 1
for k in range(0,q):
	x,y = map(int,raw_input().split())
	if a[x - 1][y - 1] == 1:
			intact = intact - 1
			if x >=  2:
				for d in range(2,x):
					if x - d >= 0 and a[x - d][y - 1] == 1:
						intact = intact - 1 
			if y >=  2:
				for d in range(2,y):
					if y - d >= 0 and a[x - 1][y - d] == 1:
						intact = intact - 1 
			if x + 1 <= n:
				for d in range(x,n):
					if d + 1 <= n and a[d][y - 1] == 1:
						intact = intact - 1 
			if y + 1 <= m:
				for d in range(y,m):
					if d + 1 <= m and a[x - 1][d] == 1:
						intact = intact - 1 
	print intact

