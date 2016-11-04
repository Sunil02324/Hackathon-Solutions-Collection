t = int(raw_input())
while t >0:
	t = t-1
	n = int(raw_input())
	a= map(int,raw_input().split())
	a.sort()
	rer = False
	for i in range(0,n-1):
		if a[i+1] - a[i]  <= 1:
			rer = False
		else:
			rer = True 
			break
	if rer:
		print "NO"
	else:
		print "YES"

