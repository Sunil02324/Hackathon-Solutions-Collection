t = int(raw_input())
while (t>0):
	t = t -1
	a = list(raw_input())
	n = len(a)
	for i in range(0, n-1):
		j = n -1 - i
		if(a[i] == '.' and a[j] != '.'):
			a[i] = a[j]
		elif(a[i] != '.' and a[j] == '.'):
			a[j] = a[i]
		elif(a[i] == '.' and a[j] == '.'):
			a[i] = a[j] = 'a'
		elif(a[i] != a[j]):
			a = '-1'
			break
	print "".join(a)