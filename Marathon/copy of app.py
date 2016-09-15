t = int(raw_input())
while t>0:
	t = t-1
	def det(a, b):
	    return a[0] * b[1] - a[1] * b[0]
	line1 = [[] for i in range(2)]
	line2 = [[] for i in range(2)]
	g = map(int,raw_input().split())
	line1[0] = [g[0],g[1]]
	line1[1] = [g[2],g[3]]
	line2[0] = [g[4],g[5]]
	line2[1] = [g[6],g[7]]
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) 
	div = det(xdiff, ydiff)
	if div == 0:
	       print "-1"
	else:
		    d = (det(*line1), det(*line2))
		    x = float(det(d, xdiff) / div)
		    y = float(det(d, ydiff) / div)
		    x = round(x,1)
		    y = round(y,1)
		    print str(x) + ' ' + str(y)



from numpy import *
def perp( a ) :
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )
    if (denom == 0 or db in None):
    	return "-1"
    else:
	    z = (num / denom.astype(float))*db + b1
	    return str(z[0]) + ' ' + str(z[1])


t = int(raw_input())
while t>0:
	t = t-1
	g = map(int,raw_input().split())
	p1 = array( [g[0],g[1]] )
	p2 = array( [g[2],g[3]] )

	p3 = array( [g[4],g[5]] )
	p4 = array( [g[6],g[7]] )

	print seg_intersect( p1,p2, p3,p4)