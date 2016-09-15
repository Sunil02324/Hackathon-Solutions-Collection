n = int(raw_input())
while n>0:
	n = n-1
	a = []
	a = set(raw_input())
	vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	if any(char in vowels for char in a):
		print "Neha wins"
	else:
		print "Shilpa wins"