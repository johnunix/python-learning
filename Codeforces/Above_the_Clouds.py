t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    found = False
    for i in range(1, len(s)-1):
        if s[i] in s[:i] or s[i] in s[i+1:]:
            found = True
            break
    print("Yes" if found else "No") 
