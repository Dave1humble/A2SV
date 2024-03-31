if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    runner_upscore = sorted(arr, reverse=True)
    output = runner_upscore[1]
    print(output)
