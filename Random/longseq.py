t = int(raw_input())
for i in range(0,t):
	a = map(int,raw_input())
	x = 0
	y = 0
	for ch in a:
		if(ch == 1):
			x += 1
		elif(ch == 0):
			y += 1
	if (x == 1 or y == 1):
		print 'Yes'
	else:
		print 'No'