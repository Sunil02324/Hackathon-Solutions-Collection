n = int(raw_input())
a = raw_input().split()
done = True
for i in range(0,n-1):
	if int(a[i+1]) >= int(a[i]):
		done = True
	else:
		done = False
		break
if done:
	print "Happy"
else:
	print "Angry"
