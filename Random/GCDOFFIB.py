from fractions import gcd
mem = dict()

def fib(n):
    if n <= 2:
        return 1
    if n in mem:
        return mem[n]
    k = n/2
    a = fib(k + 1)
    b = fib(k)
    ans = 0
    if n % 2 == 1:
        ans = a*a + b*b
    else:
        ans = b*(2*a - b)
    mem[n] = ans
    return ans


n = int(raw_input())
s = [[]]*n
m = 1000000007
for i in range(0,n):
	s[i] = map(int,raw_input().split())
k = int(raw_input())
t = k
while t > 0:
	t = t-1
	d = map(int,raw_input().split())
	if d[0] == 0:
		s[d[1]-1] = [d[2],d[3]]
	elif d[0] == 1:
		score = 0
		for i in range(d[1],d[2]+1):
			value = gcd(fib(s[i-1][0]), fib(s[i-1][1]))%m
			if value >score:
				score = value
		print score,

