def backpack(stocks, volume):
    stocks_sorted = sorted(stocks, key=lambda x: x[0] / x[1], reverse=True)
    result = 0
    current_stock = 0
    while volume > 0 and current_stock < len(stocks_sorted):
        if volume > stocks_sorted[current_stock][1]:
            result += stocks_sorted[current_stock][0]
            volume -= stocks_sorted[current_stock][1]
        else:
            result += stocks_sorted[current_stock][0] * (volume / stocks_sorted[current_stock][1])
            volume = 0

        current_stock += 1
    return result

# print("%.3f" % backpack([[60, 20], [100, 50], [120, 30]], 50))

(n, volume) = list(map(int, input().split(" ")))
stocks = []
for i in range(n):
    stocks.append(list(map(int, input().split(" "))))

print("%.3f" % backpack(stocks, volume))
