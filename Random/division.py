limit = 1000000
primes = []
count_primes = 0 
 
def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
 
def is_prime(d):
    return d in primes
 
t = int(raw_input())
primes = list(sieve(limit))
count_primes = len(primes)
for i in range(0,t):
	n,m = map(int,raw_input().split())
	b = map(int,raw_input().split())

	output = ""
 
 
	def LeastPrimeDivisor(z):
		for i in range(0, count_primes):
			if(z%primes[i]==0):
				return primes[i]
		return z
 
 
	def update(L,R):
		for k in range(L,R + 1):
			b[k - 1] = b[k - 1] / LeastPrimeDivisor(b[k - 1])
 
 
	def get(L,R):
		result = 1
		for j in range(L,R + 1):
			result = max(result, LeastPrimeDivisor(b[j - 1]))
		return result
 
 
	for i in range(0,m):
		ty, X, Y = map(int,raw_input().split())
		if ty == 0:
			update(X,Y)
			#print b
		else :
			output += str(get(X,Y)) + " "
	print output