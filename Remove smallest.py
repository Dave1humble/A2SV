t = int(input())
output = []
for _ in range(t):
    o = True
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        output.append("YES")
        continue
    a.sort()
    for j in range(1, n):
        if a[j] - a[j-1] > 1:
            o = False
            break
    output.append("YES" if o else "NO")
 
print('\n'.join(output))
