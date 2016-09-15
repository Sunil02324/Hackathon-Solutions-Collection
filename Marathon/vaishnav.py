n = int(raw_input())
a = map(int, raw_input().split())
z = 0

seen = set()
uniq = []
for x in a:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
        c = a.count(x)
        if (c%2 == 0):
        	d = int(c/2)
        else:
        	c = c-1
        	d = int(c/2)
        z = z + d
if (z>0):
	print z-1
else:
	print "-1"