# Running for codechef 0.06 14mb

T = int(input())

for _ in range(T):
    n = int(input())
    timetable = list(map(int, input().split(" ")))
    time_req = list(map(int, input().split(" ")))

    time = count = 0

    for i in range(n):
        if abs(timetable[i] - time) >= time_req[i]:
            count += 1

        time = timetable[i]

    print(count)
