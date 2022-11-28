f = []
for i in range(n):
    f.append([ch for ch in input()])

(y1, y2) = [i for i, x in enumerate(line) if x == "*"]

n = int(input())
(n, k) = list(map(int, input().split()))

d = list(map(int, input().split()))
