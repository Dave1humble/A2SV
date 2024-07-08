from collections import defaultdict

# Read input
n, m = map(int, input().split())
na = [input().strip() for _ in range(n)]
mb = [input().strip() for _ in range(m)]

# Initialize the defaultdict with list
d = defaultdict(list)

# Fill the defaultdict with positions of words in na (group A)
for index, word in enumerate(na):
    d[word].append(index + 1)  # index + 1 for 1-based indexing

# For each word in mb (group B), print positions or -1 if not found
for word in mb:
    if word in d:
        print(' '.join(map(str, d[word])))
    else:
        print(-1)
