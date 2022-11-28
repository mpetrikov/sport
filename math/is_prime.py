import math

def isPrime(n):
    isPrime = True
    for i in range(2, math.sqrt(n) + 1):
        if n % i == 0:
            isPrime = False
    return isPrime
