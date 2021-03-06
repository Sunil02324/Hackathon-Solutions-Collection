import sys
 
def compute(mat, n, k):
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j == 1:
                mat[i][j] = pow(2, i) - 1
                continue
            if i - j - 1 >= 0:
                mat[i][j] = 2 * mat[i - 1][j] + (pow(2, i - j - 1) - mat[i - j - 1][j])
            elif i - j == 0:
                mat[i][j] = 1
 
n, k = map(int,raw_input().split())
mat = [[0 for i in range(k + 1)] for i in range(n + 1)]
compute(mat, n, k)
num = mat[n][k]
denom = pow(2, n)
while (num & 0x1 == 0):
    num >>= 1
    denom >>= 1
print("%d/%d" % (num, denom))
