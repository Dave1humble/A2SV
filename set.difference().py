number_of_english = int(input())
space_separated1 = set(map(int, input().split()))

number_of_france = int(input())
space_separated2 = set(map(int, input().split()))


only_english_subscribers = space_separated1.difference(space_separated2)


print(len(only_english_subscribers))
