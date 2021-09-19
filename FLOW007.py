N = int(input())


def reverse(num) -> int:
    rev = 0
    while(num > 0):
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem
    return rev


for i in range(N):
    num = int(input())
    print(reverse(num))
