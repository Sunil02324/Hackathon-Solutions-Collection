t = int(raw_input())
while t> 0:
	t =t - 1
	N = int(raw_input())
	a = map(int,raw_input().split())
	s = int(raw_input())
	x=0
	i=0
	d = []
	if(N%2==0):
		while (i < N/2 and x<s):
			x=x+a[i]
			d.append(i+1)
			if(x<s):
				x=x+a[N-1-i]
				d.append(N-i)
			i=i+1
	else:
		while (i < N/2+1 and x<s):
			x=x+a[i]
			d.append(i+1)
			if(i!= N/2+1 and x<s): 
				x = x+a[N-1-i]
				d.append(N-i)
			i=i+1
	if x == s:
		for c in d:
			print str(c),
	else:
		print 'BING'