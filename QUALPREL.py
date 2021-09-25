# second try at this problem

T = int(input())

for _ in range(T):
    N, K = map(int, input().split(" "))
    q = list(map(int, input().split(" ")))

    q.sort(reverse=True)
    benchmark = q[K-1]

    i = count = 0

    try:
        while(q[i] >= benchmark):
            count += 1
            i += 1

    except IndexError:
        pass

    print(count)
