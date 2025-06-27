import math
def check(l1, b1, l2, b2, l3, b3):
    Area = l1* b1 + l2*b2 + l3 *b3
    s = int(math.isqrt(Area))
    if s*s != Area:
        return False
    
    if l1 == l2 == l3 == s and b1+b2+b3 == s or b1 == b2 == b3 == s and l1+l2+l3 == s:
        return True
    
    if l1 == s:
        remaining_breadth = s - b1
        if (l2+l3 ==s and b2 == b3 == remaining_breadth):
            return True
    
    if b1 == s:
        remaining_legth = s - l1
        if (b2+b3 == s and l2 == l3 == remaining_legth):
            return True
    else:
        return False


t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    print("Yes" if check(l1, b1, l2, b2, l3, b3) else "No")
