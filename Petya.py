def Petya(str1, str2):
    n = len(str1)
    flag = 0
    for i in range(n):
        if str1[i].lower() == str2[i].lower():
            pass
        elif str1[i].lower() < str2[i].lower():
            print("-1")
            flag += 1
            break
        elif str1[i].lower() > str2[i].lower():
            flag += 1
            print("1")
            break
    if flag == 0:
        print("0")


Petya(input(), input())
