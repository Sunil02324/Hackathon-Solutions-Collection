t = int(raw_input())
while t>0:
	t = t-1
	x1,y1,x2,y2 = map(int,raw_input().split())
	if x1 != x2 and y1 != y2:
		print "sad"
	else:
		if x1 == x2:
			if y1>y2:
				print  "down"
			else:
				print "up"
		elif y1 == y2:
			if x1>x2:
				print "left"
			else:
				print "right"