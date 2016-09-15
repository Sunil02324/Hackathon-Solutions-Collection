import math
limit = 1000000
primes = []
divisors = []
def GeneratePrimes():
	divisors.append(1)
	divisors.append(2)
	primes.append(2)
	divisors.append(3)
	primes.append(3)
	for i in range(4,limit + 1):
		flag = 0
		p = 0
		l = math.sqrt( i )
		while primes[p] <= l:
			if i%primes[p] == 0:
				flag = 1
				divisors.append(primes[p])
				break
			p += 1
		if flag == 0:
			divisors.append(i)
			primes.append(i)

def update(b, L,R):
		for k in range(L,R + 1):
			b[k] = b[k] / divisors[b[k] - 1]
 
 
def get(b, L,R):
	result = 1
	for j in range(L,R + 1): 
		result = max(result, divisors[b[j] - 1])
	return result
 
 
GeneratePrimes()
t = int(raw_input())
while (t>0):
	t = t -1
	n,m = map(int,raw_input().split())
	b = map(int,raw_input().split())
	output = ""
	for i in range(0,m):
		ty, X, Y = map(int,raw_input().split())
		if ty == 0:
			update(b, X - 1,Y - 1)
		else :
			output += str(get(b, X - 1,Y - 1)) + " "
	print output 