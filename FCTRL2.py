def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


T = int(input())
for _ in range(T):
    n = int(input())
    print(factorial(n))
