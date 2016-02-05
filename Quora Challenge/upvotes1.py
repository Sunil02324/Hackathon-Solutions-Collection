n, k = map(int, raw_input().split())

upvotes = map(int, raw_input().split())

non_decreasing = [[0]*n for i in [1,2]]
non_increasing = [[0]*n for i in [1,2]]
num_non_dec_sequences = 0
num_non_inc_sequences = 0

for i in range(0, n):
    non_decreasing[0][i] = 1 + (non_decreasing[0][i-1] if (i and (upvotes[i] >= upvotes[i-1])) else 0)
    non_increasing[0][i] = 1 + (non_increasing[0][i-1] if (i and (upvotes[i] <= upvotes[i-1])) else 0)

for i in range(n-1, -1, -1):
    non_decreasing[1][i] = 1 + (non_decreasing[1][i+1] if ((i < n-1) and (upvotes[i] >= upvotes[i+1])) else 0)
    non_increasing[1][i] = 1 + (non_increasing[1][i+1] if ((i < n-1) and (upvotes[i] <= upvotes[i+1])) else 0)


for i in range(0, k-1):
    num_non_dec_sequences += non_decreasing[0][i]
    num_non_inc_sequences += non_increasing[0][i]


for i in range(k-1, n):
    num_non_dec_sequences += min([k, non_decreasing[0][i]])
    num_non_inc_sequences += min([k, non_increasing[0][i]])

    print (num_non_dec_sequences - num_non_inc_sequences)
    num_non_dec_sequences -= min([k, non_increasing[1][i-k+1]])
    num_non_inc_sequences -= min([k, non_decreasing[1][i-k+1]])