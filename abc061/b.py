n, m = map(int, input().split())
arr = [0] * n

for _ in range(m):
    x, y = map(int, input().split())
    arr[x - 1] += 1
    arr[y - 1] += 1

for ele in arr:
    print(ele)
