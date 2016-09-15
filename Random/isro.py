from __future__ import print_function
import re
import operator
from collections import Counter
from math import factorial
def npermutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return int(num/den)

t = int(raw_input())
	
for i in range(0,t):
	d = raw_input()
	s = re.sub("[^a-zA-Z]+", "", d)
	k = list(s)
	z = npermutations(k)
	print (int(z))
	