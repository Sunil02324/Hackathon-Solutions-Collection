n = int(raw_input())
s = list(raw_input())
count = 0
a = [[]]
b = [[]]
a.append([0,0])
b.append([0,0])
count += 1
x = 0
y = 0
p = 0
q = 0
for i in range(0,n,2):
	if s[i] == 'U':
		y += 1
		if [x,y] not in a:
			if [x,y] not in b:
				a.append([x,y])
				count += 1
	elif s[i] == 'D':
		y -= 1
		if [x,y] not in a:
			if [x,y] not in b:
				a.append([x,y])
				count += 1
	elif s[i] == 'L':
		x -= 1
		if [x,y] not in a:
			if [x,y] not in b:
				a.append([x,y])
				count += 1
	elif s[i] == 'R':
		x += 1
		if [x,y] not in a:
			if [x,y] not in b:
				a.append([x,y])
				count += 1

	if s[i+1] == 'U':
		q += 1
		if [p,q] not in b:
			if [p,q] not in a:
				b.append([p,q])
				count += 1
	elif s[i+1] == 'D':
		q -= 1
		if [p,q] not in b:
			if [p,q] not in a:
				b.append([p,q])
				count += 1
	elif s[i+1] == 'L':
		p -= 1
		if [p,q] not in b:
			if [p,q] not in a:
				b.append([p,q])
				count += 1
	elif s[i+1] == 'R':
		p += 1
		if [p,q] not in b:
			if [p,q] not in a:
				b.append([p,q])
				count += 1

print count