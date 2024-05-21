def sign(num):
    return 1 if num > 0 else -1
 
t = int(input())
results = []  
for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    max_sum = 0
    current_max = seq[0]
    for i in range(1, len(seq)):
        if sign(seq[i]) == sign(current_max):
            current_max = max(current_max, seq[i])
        else:
            max_sum += current_max
            current_max = seq[i]
    max_sum += current_max
    results.append(max_sum) 
for result in results:
    print(result)
