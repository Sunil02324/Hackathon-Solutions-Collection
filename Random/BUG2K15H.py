import string
t = int(raw_input())
while (t>0):
	t = t -1
	a = list(raw_input())
	b = [0]*26
	for x in a:
		pos = string.lowercase.index(x)
		b[pos] += 1
	output = ''
	for i in range(0,26):
		if b[i] > 0 :
			if b[i] == 1:
				output += chr(ord('a') + i)
			else:
				output += chr(ord('a') + i) + str(b[i])
	print output
