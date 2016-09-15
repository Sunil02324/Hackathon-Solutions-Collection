from __future__ import division
n = int(raw_input())
p,q = map(int,raw_input().split())
m = int(raw_input())
r,s = map(int, raw_input().split())

a = []
b = []
if(n>m):
	for i in range(1,n+1):
		sup = (p**i)%q
		a.append(int(sup))
	a = sorted(a,reverse=True)
	for j in range(1,m+1):
		bat = (r**j)%s
		b.append(bat)
	b = sorted(b,reverse=True)
	sub = 0
	for l in range(0,m):
		sub += a[l] - b[l]
	sub = float(int(sub)/2)
	print("%.1f" % sub)