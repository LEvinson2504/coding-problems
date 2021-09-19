string = input()

seen_chars = []

for i in string:
    if i not in seen_chars:
        seen_chars.append(i)
    else:
        pass

if len(seen_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
