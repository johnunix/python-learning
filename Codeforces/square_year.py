import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = int(math.sqrt(n))

    if l*l != n:
        print(-1)

    else:
        print(f"{0} {l}")
