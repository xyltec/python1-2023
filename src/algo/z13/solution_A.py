def get_decomposition(n, k, x) -> list:
    if n <= 0: return []
        
    else:
        decomposition = []
        while n >= k:
            if n == x: return []
            if k > 0: decomposition.append(k)
            n -= k

        if n != x:
            if n > 0: decomposition.append(n)

        else: return []

        return decomposition