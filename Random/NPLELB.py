n,x = map(int,raw_input().split())
striker = 0
unstriker = 0
total = 0
a = ['']*100000
for i in range(0,n):
	a[i] = raw_input()
	if a[i] == '-1':
		print str(striker) + " " + str(total) + " "
		striker = 0
	else:
		total += int(a[i])
		striker += int(a[i])
		if int(a[i])%2 != 0:
			striker, unstriker = unstriker,striker
	if (i+1)%x == 0:
		striker, unstriker = unstriker,striker
print total