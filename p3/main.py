f = open('INPUT.txt', 'r')
text = f.read()
lines = text.split('\n')

num = int(lines.pop(0))



words = []
set = []
for i in range(num):
    set.append(lines[i])
def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C
print LCS('numb','nom')