def canChef(numbers, sum, n):
	if sum == 0:
		return True
	if n == 0 and sum != 0:
		return False
	if numbers[n-1] > sum:
		return canChef(numbers,sum, n-1)
	return canChef(numbers, sum, n - 1) or canChef(numbers,sum - numbers[n-1],n - 1)

t = int(raw_input())
while (t>0):
	t = t -1
	n,k = map(int,raw_input().split())
	a = map(int,raw_input().split())
	if canChef(a,k,n):
		print 'YES!'
	else:
		print 'NO!'