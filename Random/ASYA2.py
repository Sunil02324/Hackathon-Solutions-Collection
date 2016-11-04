n,m = map(int, raw_input().split())
a = ['']*n
b = ['']*m
for i in range(0,n):
	a[i] = raw_input()
for i in range(0,m):
	b[i] = raw_input()
c = []
for i in range(0,n):
	for j in range(0,m):
		c.append(a[i]+b[j])
d = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
present = True
count = 0
for x in c:
	for y in d:
		if y in x:
			present = True
		else:
			present = False
			break
	if present:
		count += 1
print count
