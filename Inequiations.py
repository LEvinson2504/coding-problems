def Solve():
    n, x, y = map(int, input().split())
    for i in range(n):
        sum = flag = 0
        for j in range(i):
            sum += j**2
            if sum < x or sum > y:
                print("-1")
                flag += 1

            if flag == 0:
                print(j)


Solve()
