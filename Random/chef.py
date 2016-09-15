from __future__ import print_function
n = int(raw_input())

a = []
a = raw_input().split()
l = list(range(0,n+1))
#print (l)
#print (i for i in l if i in a, end=" ")
c = [i for i in l if str(i) not in a]
#print (c)
for j in c:
	print (j, end=" ")
#for i in range(0,n+1):
#	if str(i) in a:
#		continue
#	else:
#		print (i, end=" ")