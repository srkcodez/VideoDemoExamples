def add(m, n):
    if n == 0:
        return m
    else:
        res = add(m, n - 1) + 1
        return res


a = add(25, 5)
print(a)
