t = int(raw_input())
def line_intersection(line1, line2):
	    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) 

	    def det(a, b):
	        return a[0] * b[1] - a[1] * b[0]

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

while t>0:
	t = t-1
	
	line1 = [[] for i in range(2)]
	line2 = [[] for i in range(2)]
	g = map(int,raw_input().split())
	line1[0] = [g[0],g[1]]
	line1[1] = [g[2],g[3]]
	line2[0] = [g[4],g[5]]
	line2[1] = [g[6],g[7]]

	line_intersection(line1, line2)