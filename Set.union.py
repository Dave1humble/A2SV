number_english = int(input())
roll_english = set(list(map(int, input().split())))
number_french = int(input())
roll_french = set(list(map(int, input().split())))

print(len(roll_english.union(roll_french)))
