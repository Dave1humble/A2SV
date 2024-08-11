n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i, j = 0, 0
res = []
while i < n and j < m:
    if arr1[i] < arr2[j]:
        res.append(arr1[i])
        i += 1
    else:
        res.append(arr2[j])
        j += 1


while i < n:
    res.append(arr1[i])
    i += 1

while j < m:
    res.append(arr2[j])
    j += 1

print(' '.join(map(str, res)))
