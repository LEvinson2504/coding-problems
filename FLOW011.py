T = int(input())
for _ in range(T):
    BS = int(input())
    HRA, DA = 0, 0

    if BS < 1500:
        HRA = 0.1 * BS
        DA = 0.9 * BS

    else:
        HRA = 500
        DA = 0.98 * BS

    print(BS+HRA+DA)
