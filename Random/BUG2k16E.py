def sum(N):
	s=0
	for x in range(1,N+1):
		s=s+x
	return s

def ans(N,k):
	s = sum(N)
	p=1
	while N > pow(k,p):
		s = s - pow(k,p)
		p = p+1
	return s

t = int(raw_input())
for i in range(0,t):
	case = i + 1
	n,k = map(int,raw_input().split())
	print 'Case #' + str(case) + ': ' + str(ans(n,k))