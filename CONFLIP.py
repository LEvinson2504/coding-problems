# Input
# 1
# 2
# 1 5 1
# 1 5 2

# [H,T,H,T,H,T]
# [h,t,h,t,h]

ts = int(input())
g = int(input())
h = t = 0
for _ in range(ts):
    input_list = input().split(" ")
    I = int(input_list[0])
    N = int(input_list[1])
    Q = int(input_list[2])

    if (N % 2 == 0):
        h = t = N // 2
    else:
        h = N//2 + 1

    if (Q == 1):
        print(h)
    else:
        print(t)
