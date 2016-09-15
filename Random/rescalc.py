t = int(raw_input())
while (t>0):
	t = t -1
	n = int(raw_input())
	tie = False
	winner = 0
	score = 0
	for i in range(0,n):
		a = map(int,raw_input().split())
		ncookies = a[0]
		nscore = ncookies
		a.pop(0)
		b = [0]*7
		for j in a:
			b[j] += 1
		b.sort()
		bonus = 4*b[1] + 2*(b[2] - b[1]) + (b[3] - b[2])
		nscore += bonus
		if(nscore > score):
			winner = i
			score = nscore
			tie = False
		elif(nscore == score):
			tie = True
	if(tie == True):
		print "tie"
	else:
		if(winner == 0):
			print "chef"
		elif (winner > 0):
			print winner + 1