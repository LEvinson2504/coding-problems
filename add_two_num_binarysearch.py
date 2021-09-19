import math

def solve(nums: list, k: int):
    nums.sort()

    #hm: dict = {num: math.fabs(k - num) for num in nums }
    hm: dict = {}

    for i in hm.items():
        if i[0] not in iter(hm):
            hm[i] = math.fabs(k - i[0])

        if hm.get(i[1]): 
            return True

    print(hm)
                     
    return False

if solve([1,2,3,4], 5):
    print("works")
