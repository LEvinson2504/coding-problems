S = int(input())

def check_equal_and_increment(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if i > 0:
            if abs(arr1[i-1] - arr1[i]) > 1:
                return False

            if abs(arr2[i-1] - arr2[i]) > 1:
                return False
            

        if arr1[i] != arr2[i]:
            return False

    return True

for _ in range(S):
    N = int(input())
    heights = list(map(int, input().split(" ")))
    

    if (N % 2) == 0 or N < 3:
        print("no")
        continue

    if (heights[0] != 1) and (heights[N-1] != 1):
        print("no")
        continue

    # check if it is mirrored 
    mid = (N // 2) + 1
    arr1 = heights[:mid-1]
    arr2 = heights[mid:]
    arr2.reverse()
    if check_equal_and_increment(arr1, arr2):
        print("yes")
        continue

    print("no")

