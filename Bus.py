def Solve():
    n = int(input())
    seats = ""
    for _ in range(n):
        seats += input() + "\n"

    if "OO" in seats:
        seats_after = seats.replace("OO", "++", 1)
        print(seats_after)

    else:
        print("NO")


Solve()
