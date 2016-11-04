q = int(raw_input())
n = 1000
studs =  [[]]*n
while (q>0):
	q = q -1
	t, m, r, p = raw_input().split()
	if int(t) == 1:
		studs[int(m) - 1] = [p, int(r)]
	if int(t) == 2:
		count = 0
		for i in range(int(m) - 1,int(r)):
			if len(studs[i]) != 0 and studs[i][0] == p:
				count += studs[i][1]
		print count