data = [5, 4, 3, 2, 1]

count_arr = [0] * 201
# print(len(count_arr))
for i in range(len(data)):
    count_arr[data[i]] += 1

# construct arr from count_arr
# ...


def find_med_in_counting_arr(arr):
    ssum = sum(arr)

    if ssum % 2 == 0:
        half_sum = ssum / 2
        half_sum_plus_one = ssum / 2 + 1
        count = 0
        result = 0
        for i in range(201):
            if result == 0 and count + arr[i] >= half_sum:
                result += i
            if count + arr[i] >= half_sum_plus_one:
                result += i
                return result / 2
            count += arr[i]
    else:
        half_sum = ssum / 2
        count = 0
        for i in range(201):
            if count + arr[i] > half_sum:
                return i
            count += arr[i]
    return 0