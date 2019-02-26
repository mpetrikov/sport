import sys

def find_pos(xs, query):
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (hi + lo) // 2
        if query < xs[mid]:
            hi = mid
        elif query > xs[mid]:
            lo = mid + 1
        else:
            return mid

    return -1

def test():
    assert find_pos([], 23) == -1
    assert find_pos([11], 11) == 0
    assert find_pos([11], 13) == -1

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")


if __name__ == '__main__':
    main()
