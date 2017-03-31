n = int(raw_input())
count = 0


for i in range(0,n):
	count = 0
	space = raw_input()
	h,w = raw_input().split(' ')
	maze = []
	for j in range(0,int(h)):
		maze.append(list(raw_input()))
	def DeadMaze(h1,w1,maze,h,w,count):
		if 1 < h1 < h  and maze[h1+1][w1] == '.' and DeadMaze(h1+1,w1,maze,h,w,count):
			return True
		# if h1 < h and maze[h1-1][w1] == '.' and DeadMaze(h1-1,w1,maze,h,w,count):
		# 	return True
		if 1< w1 < w and maze[h1][w1+1] == '.' and DeadMaze(h1,w1+1,maze,h,w,count):
			return True
		# if w1 < w and maze[h1][w1-1] == '.' and DeadMaze(h1,w1-1,maze,h,w,count):
		# 	return True
		count += 1
		return False

	if DeadMaze(2,2,maze,int(h),int(w),count):
		#Nothing
		count = count
	else:
		count += 1
	print "Case #" + str(i+1) + " " + str(count)
