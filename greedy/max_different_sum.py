def s(n):
    current_n = 1
    result = []
    while n > 0:
        if n >= 2 * current_n + 1:
            result.append(current_n)
            n -= current_n
            current_n += 1
        else:
            result.append(n)
            n = 0
    return result


result = s(20)
print(len(result))
print(" ".join(map(str, result)))
