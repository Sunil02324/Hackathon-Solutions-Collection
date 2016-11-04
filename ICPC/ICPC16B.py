t = int(raw_input())
while t>0:
	t=t-1
	n = int(raw_input())
	k=n
	a = map(int,raw_input().split())
	p=0
	for i in range(0,n-1):
		for j in range(i+1,n):
			if a[i]*a[j] not in a:
				p=1
				break
	if p==1:
		print "no"
	else:
		print "yes"