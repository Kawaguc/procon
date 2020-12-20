def extgcd(a, b):
    """
    拡張ユークリッドの互除法
    ax+by=gcd(a,b)に対して(gcd,x,y)を返す
    """
    if b == 0:
        return a, 1, 0
    g, x, y = extgcd(b, a % b)
    return g, y, x - a // b * y
