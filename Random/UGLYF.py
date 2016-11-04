t = int(raw_input())
while t > 0:
    t = t-1
    a = raw_input()
    b = raw_input()
    mina = 10000000000000000
    i=0
    for p in a:
        i+=1
        j=0
        if p in b:
	        for g in b:
	            j+=1
	            if p==g:
	                L1 = i-1
	                L2 = j-1
	                L3 = len(a) - i
	                L4 = len(b) - j
	                z = abs(L1-L2)+abs(L2-L3)+abs(L3-L4)+abs(L4-L1)
	                if z< mina:
	                	mina = z
    print z