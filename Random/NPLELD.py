n = int(raw_input())
a = map(int,raw_input().split())
#print a
q = int(raw_input())
for i in range(0,q):
	k = int(raw_input())
	count = 0
	for j in range(0,n-1):
		for z in range(j+1,n):
			#print str(j) + " " + str(z)
			l = a[j]*a[z]
			if k%l == 0:
				count += 1
	print count
