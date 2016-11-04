def sumd(s):
	k = 0
	while s != 0:
		k += s%10
		s  = s/10
	return k


t = int(raw_input())
while t>0:
	t = t-1
	d = int(raw_input())
	if d<9:
		print d + 1
	elif d ==9:
		print 1
	elif d>9:
		e = 0
		i = 0
		while i >= 0:
			e = i*10 + 9;
			i !=
            if sumd(e) == d:
                print e
                i = -1
