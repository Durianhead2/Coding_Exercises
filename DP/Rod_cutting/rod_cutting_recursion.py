price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cutRod(p, n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cutRod(p, n - i))
    return q

print(cutRod(price, 10))