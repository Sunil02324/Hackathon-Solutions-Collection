# def subsum(a,n,m):
# 	if(n==0 and m!=0):
# 		return False
# 	if(m==0):
# 		return True
# 	if(a[n-1]>m):
# 		return subsum(a,n-1,m)
# 	return subsum(a,n-1,m) or subsum(a,n-1,m-a[n-1])
 
# t=int(raw_input())
# for j in range(t):
# 	n,m=map(int,raw_input().split())
# 	a=map(int,raw_input().split())
# 	a.sort()
# 	print ['NO!','YES!'][subsum(a,n,m)]

def check_vals(m,data):
    j = False
    if m in data:
        return True
    elif data:        
        k = data[0]
        while k>m:
            data.pop(0)
            if data:
                k = data[0]
            else:
                return False
        for i in range(len(data)):
            j = check_vals(m-data[i],data[i+1:])
            if j:
                break
        if j:
            return True
        else:
            return check_vals(m-data[0],data[1:])
                
l = int(raw_input())
for z in range(l):
    n,m = map(int,raw_input().split())
    data = map(int,raw_input().split())
    data.sort(reverse=True)
    j = False
    if m in data:
        j = True
    else:
        for i in range(n):
            j = check_vals(m-data[i],data[i+1:])
            if j:
                break
        
    if j:
        print 'YES!'
    else:
        print 'NO!' 