n = int(raw_input())
while n>0:
	n = n-1
	l,b,r = map(int, raw_input().split())
	if (r<=l and r<=b):
		print "Yes"
	else:
		print "No"