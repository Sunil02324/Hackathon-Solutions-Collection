import operator
n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
b = []
c= []
d = []
for i in range(0,m):
	f,p,s = raw_input().split()
	f = int(f)
	p = int(p)
	e = []
	e.append(f)
	e.append(p)
	e.append(s)
	if int(e[0]) in a:
		c.append(e)
	else:
		d.append(e)
# c.sort(key=lambda x: x[1], reverse = True)
# d.sort(key=lambda x: x[1], reverse = True)
sorted(c, key=operator.itemgetter(2), reverse=True)
sorted(d, key=operator.itemgetter(2), reverse=True)
print c
print d
for z in c:
	print  z[2] 
for x in d:
	print x[2]
