word = input()
n = len(word) // 2
low = upp = 0

for i in word:
    if low > n:
        print(word.lower())
        break

    if upp > n:
        print(word.upper())
        break

    if i.islower():
        low = low + 1
    elif i.isupper():
        upp = upp + 1
