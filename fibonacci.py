a = 1
b = 2
fib = [1, 2]

while b < 20000:
    a, b = b, a+b
    fib.append(b)
