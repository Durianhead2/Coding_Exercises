price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def memoized_cut_bottomup(p, n):
    """
    Calculates the maximum revenue that can be generated
    from cutting a rod in different ways.
    :param p: price array for rods of different lengths
    :param n: length of original rod
    """ 
    max_rev = [-float('inf')] * (n + 1)
    max_rev[0] = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            max_rev[i] = max(max_rev[i], max_rev[i-j] + p[j-1])
    return max_rev[n]

print(memoized_cut_bottomup(price, 10))