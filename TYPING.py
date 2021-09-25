# 1
# 5
# fdjkd
# dfjdk
# dfd
# fdjkd
# kkjjk

import math

T = int(input())

for _ in range(T):
    n = int(input())
    wordlist = []
    left = ["d", "f"]
    right = ["j", "k"]
    prev_word = {}
    for _ in range(n):
        wordlist.append(input())

    total_time = 0
    for word in wordlist:
        time = 0.2

        if word in prev_word:
            time = prev_word[word] / 2
        else:
            for i in range(1, len(word)):
                if ((word[i] in left) and (word[i-1] in left)) or ((word[i] in right) and (word[i-1] in right)):
                    time = math.fsum([time, 0.4])
                else:
                    time = math.fsum([time, 0.2])
            prev_word[word] = time

        total_time = math.fsum([total_time, time])
    print(total_time)
