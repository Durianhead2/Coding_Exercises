price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def memoized_cut_rod(p, n):
    max_rev = [-float('inf')] * (n + 1)
    return memoized_cut_rod_aux(p, n, max_rev)

def memoized_cut_rod_aux(p, n, max_rev):
    if max_rev[n] >= 0:
        return max_rev[n]
    elif n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n+1):
            q = max(q, p[i-1] + memoized_cut_rod_aux(p, n-i, max_rev))
    max_rev[n] = q
    return q

print(memoized_cut_rod(price, 10))
