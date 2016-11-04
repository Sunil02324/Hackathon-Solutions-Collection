from collections import defaultdict

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen, t_path))
    return paths

k = int(raw_input())
while k>0:
	k = k-1
	n,m = map(int,raw_input().split())
	path = [[]]*m
	for i in range(0,m):
		path[i] = list(raw_input().split())
	print path
	G = defaultdict(list)
	for (s,t) in path:
	    G[s].append(t)
	all_paths = DFS(G, '1')
	max_path  = max(all_paths, key=lambda l: len(l))
	# print all_paths
	# print max_path
	print len(max_path) - 2