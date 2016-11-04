n = 1000000
factorcount = [0]*n
for i in range(2,n):
	if factorcount[i] == 0:
		for j in range(i,n, i):
			factorcount[j] += 1

t = int(raw_input())
while (t>0):
	t = t -1
	x, y, k = map(int,raw_input().split())
	steps = 0
	for i in range(x, y):
		if factorcount[i] == k:
			steps += 1
	if steps > 0 :
		print steps
	else :
		print '-1'