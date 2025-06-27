t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = list(s)
    c = s.copy()
    a = []
    count = 0
    for i in range(n):
        if s[i] == '0':
            s[i] = '1'
        else:
            s[i] = '0'
        a.append(''.join(s))
        s = c.copy()
    combined_str = ''.join(a)
    for i in combined_str:
        if i == '1':
            count += 1
    print(count)
