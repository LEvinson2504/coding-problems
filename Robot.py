T = input()


def calculateSu m(n):
    if n <= 0:
        return 0
    else:
        return 2 * n + calculateSum(n - 1)


for _ in T:
    n = int(input())
    print(calculateSum(n))
