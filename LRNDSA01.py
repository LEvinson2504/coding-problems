T = int(input())


for _ in range(T):
    num = int(input())
    k = 5
    c0 = 0
    while(k <= num):
        """
        While number is still divisible by 5,
        keep dividing the number by increasing numbers
        of 5 and adding the result of resulting divisions
        """
        c0 += int(num/k)
        k *= 5
    print(c0)
