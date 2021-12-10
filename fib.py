def fb(N):
    if N == 1 or N == 2:
        return 1
    
    bottom_up = [None] * (N + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, N + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    
    return bottom_up[N]