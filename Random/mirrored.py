#from __future__ import print_function
n = int(raw_input())

for i in range(0,n):
	a,b = raw_input().split()
	a = a[::-1]
	b = b[::-1]
	c = long(a) + long(b)
	c = str(c)
	c = c[::-1]
	print c