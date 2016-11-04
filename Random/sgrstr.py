import string
t = int(raw_input())
while t>0:
	t = t - 1
	n = int(raw_input())
	s = list(raw_input())
	count = 0
	cur = 1
	for i in range(1,n):
			if (string.lowercase.index(s[i])== string.lowercase.index(s[i-1])+1) or (s[i] == 'a' and s[i-1] == 'z'):
				cur += 1
			else:
				count += (cur*(cur+1))/2
				cur =1
	count += (cur*(cur+1))/2
	print count


