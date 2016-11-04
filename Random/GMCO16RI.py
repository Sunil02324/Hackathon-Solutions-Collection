t = int(raw_input())
vowels = ('a', 'e', 'i', 'o', 'u')
for i in range(1,t+1):
	comp =raw_input()
	if comp.endswith('y'):
		print "Case#" + str(i) + ": " + comp + " is ruled by nobody."
	elif comp.endswith(vowels):
		print "Case#" + str(i) + ": " + comp + " is ruled by a queen."
	else:
		print "Case#" + str(i) + ": " + comp + " is ruled by a king."
	