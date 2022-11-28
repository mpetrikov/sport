def fib_mod(n, m):
    a = 1
    b = 1
    f = [a, b]

    if m <= 1:
        return 0

    maxPeriodSize = m * m + 1
    periodSize = 0

    for i in range(maxPeriodSize):
        # search subsequence 0,1 in positions more than 0
        a, b = b, (a + b) % m
        f.append(b)

        if a == 0 and b == 1:
            periodSize = i + 2
            break

    if n % periodSize == 0:
        return 0

    return f[(n % periodSize) - 1]


def main():
    print(fib_mod(301, 2))
    print(fib_mod(304, 5))
    print(fib_mod(309, 7))


if __name__ == "__main__":
    main()