file = open("task1-test-input.txt", "r") 
n = int(file.readline())
print n
clicks = [['A',1],['B',2],['C',3],['D',1],['E',2],['F',3],['G',1],['H',2],['I',3],['J',1],['K',2],['L',3],['M',1],['N',2],['O',3],['P',1],['Q',2],['R',3],['S',4],['T',1],['U',2],['V',3],['W',1],['X',2],['Y',3],['Z',4]]
file2 = open("output.txt","w") 
for i in range(0,n):
	texts = file.readline()
	print texts
	count = 0
	for text in texts:
		
		for click in clicks:
			if click[0] == text:
				count += click[1]
	file2.write("Case #" +str(i+1) + " " + str(count) + " \n") 
