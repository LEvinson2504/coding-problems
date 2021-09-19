T = int(input())

for _ in range(T):
    n, k = map(int, input().split(" "))
    q = list(map(int, input().split()))

    # Sort the scores
    q.sort(reverse=True)

    # Eliminate based on k Round A
    # find the score of team at k, eliminate the rest
    bench = q[k]
    # print(bench)

    count = 0
    for i in q:
        if i >= bench:
            count += 1
    print(count)
