T = input()

for _ in T:
    n = int(input())
    arr = [int(num) for num in input().split()]

    for i in range(1, len(arr) - 1):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            break

    for i in range(len(arr)):
        print(arr[i], end=" ")
