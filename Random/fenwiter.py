t = int(raw_input())
while t>0:
	t = t-1
	l1,l2,l3,n = raw_input().split()
	freq = int(n)
	dow = -1
	count = 0
	if dow == -1:
		for j in xrange(len(l3)-1, -1, -1):
			if l3[j] == '0':
				dow = j
				break
		if dow != -1:
			for j in range(0, len(l1)):
				if l1[j] == '1':
					count += 1
			temp = 0	
			for j in range(0, len(l2)):
				if l2[j] == '1':
					temp += 1	
			count += temp*freq + 1
			for j in range(0, dow+1):
				if l3[j] == '1':
					count += 1
	if dow == -1:
		for j in xrange(len(l2)-1, -1, -1):
			if l2[j] == '0':
				dow = j
				break
		if dow != -1:
			for j in range(0, len(l1)):
				if l1[j] == '1':
					count += 1
			temp = 1
			for j in range(0, dow+1):
				if l2[j] == '1':
					temp += 1	
			temp1 = 0
			for j in range(0, len(l2)):
				if l2[j] == '1':
					temp1 += 1	
			count += temp1*(freq - 1) + temp			
	if dow == -1:
		for j in xrange(len(l1) - 1, -1, -1):
			if l1[j] == '0':
				dow = j
				break
		if dow != -1:
			for j in range(0, dow+1):
				if l1[j] == '1':
					count += 1
			count += 1
 	if dow == -1:
 		count = 1
	print count	