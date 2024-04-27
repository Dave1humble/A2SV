def count_smaller_elements(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
 
n, m = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))
 
result = []
for num in array_b:
    count = count_smaller_elements(array_a, num)
    result.append(count)
 
print(*result)
