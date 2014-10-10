<<<<<<< HEAD
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
=======
def lcs(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    grid = [[0 for j in range(len2+1)] for i in range(len1+1)]
    count = 0
    for i in range(1,(len1+1)):
        for j in range(1,(len2+1)):
            if word1[i-1] == word2[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
    
def suggestion(query, word1, word2):
    first = lcs(query, word1)
    second = lcs(query, word2)
    if first >= second:
        sugg =  word1
    else: sugg = word2
    return sugg
    
f = open('INPUT.txt', 'r')
text = f.readlines()
words = []
for entry in text:
    if entry != '\n':
        words.append(entry.strip())
num = words.pop(0)
num = int(num)
ans = []
for i in range(num):
    query = words.pop(0)
    word1 = words.pop(0)
    word2 = words.pop(0)
    ans.append(suggestion(query,word1,word2))
with open('OUTPUT.txt', 'w') as f:
    for word in ans:
        f.write(word+ '\n')



>>>>>>> e6a4ec4b168f809e7adeb1c37dc161d189b30d0d
