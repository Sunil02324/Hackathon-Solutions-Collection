t = int(raw_input())
while (t>0):
	t = t -1
	n = int(raw_input())
	a = list(raw_input().split())
	print a
	b = [0]*100
	for c in a:
		b[int(c) - 1] += 1
	for i in range(0,100):
		if b[i] != 0:
			print '' + str(i +1) + ': ' + str(b[i])
