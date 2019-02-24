def cover(cuts):
    # right_points = map(lambda x: (x[1], x), cuts)
    cuts = sorted(cuts, key=lambda x: x[1])

    current_uncover_cut = 0
    current_point = cuts[current_uncover_cut][1]
    result = [current_point]

    while current_uncover_cut < len(cuts):
        if cuts[current_uncover_cut][0] <= current_point <= cuts[current_uncover_cut][1]:
            current_uncover_cut += 1
        else:
            current_point = cuts[current_uncover_cut][1]
            result.append(current_point)
            current_uncover_cut += 1

    return result

# print(cover([(4,7), (1,3), (2,5), (5, 6), (10, 13)]))


n = int(input())

cuts = []
for i in range(n):
    cuts.append(list(map(int, input().split(' '))))

result = cover(cuts)
print(len(result))
print(" ".join(map(str, result)))
