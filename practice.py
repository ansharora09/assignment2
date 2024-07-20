n=5
width = len(str((n-1)*(n-1)))     
for i in range(1,n+1):
    for j in range(1,n+1):
        x = i * j
        if (x % 2 != 0):
            print(format(x, f'>{width}'), end=",")
        else:
            print(format("x", f'>{width}'), end=" ")
    print()
