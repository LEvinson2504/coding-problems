N = int(input())

for _ in range(N):
    n = int(input())
    s1 = input()
    s2 = input()

    # 1100
    # 0011
    # if (s1.count("1") != s2.count("1")):
    #     print("No")
    #     continue

    ones = zeros = 0
    for i in range(n):
        if s1[i] != s2[i]:
            if s1[i] == "1":
                ones += 1
            else:
                zeros += 1

        if zeros != ones:
            print("No")
            continue

        print("Yes")
