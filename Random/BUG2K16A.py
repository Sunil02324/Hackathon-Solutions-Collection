t = int(raw_input())
for i in range(0,t):
	n = int(raw_input())
	case = i + 1
	score = 1
	steps = 0
	count = 0
	while count < n :
		count += score
		steps += 1
		score += 9
	print 'Case #' + str(case) + ': ' + str(steps)