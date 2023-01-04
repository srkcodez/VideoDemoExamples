def toh(n, f, t, a):
    if n == 0:
        return
    else:
        toh(n - 1, f, a, t)
        print("move disk: ", n, " from: ", f, " to: ", t)
        toh(n - 1, a, t, f)


toh(4, 'A', 'C', 'B')
