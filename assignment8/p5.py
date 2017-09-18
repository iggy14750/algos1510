
w = [50, 5, 10, 20, 25]

def min_over(M, l, r):
    best_c = r
    best = M[l][r-1]#default to c = r

    for c in range(l, r):
        temp = M[l][c-1]
        temp += M[c+1][r]
        if temp < best:
            best = temp
            best_c = c
    M[l][r] = best
    return best_c

def mwbst():
    n = len(w)
    M = [[0]*n for _ in range(n)]
    R = [[0]*n for _ in range(n)]
    for i in range(n):
        M[i][i] = w[i]
        R[i][i] = i+1
    
    for l in range(n-2, -1, -1):
        for r in range(l+1, n):
            c = min_over(M, l, r)
            M[l][r] += sum(w[l:r+1])
            R[l][r] = c+1
    for row in M:
        print(row)
    print("=====================================")
    for row in R:
        print(row)


mwbst()