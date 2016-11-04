k,t = map(int,raw_input().split())
h = []
for i in range(0,k):
	h.append(int(raw_input()))
final = sum(h)
count = 2*len(h)-1
for i in range(0,k-1):
	final += sum(h[i:i+2])
# print final
# print count
print '{0:.9f}'.format(float(final)/float(count))

