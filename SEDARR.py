N = int(input())

for i in range(N):
    n, d = input().split(" ")
    nums = input().split()

    sum = 0
    for i in nums:
        sum += int(i)

    if (sum % int(d) != 0):
        print(1)
        continue
    print(0)
