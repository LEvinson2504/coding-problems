from typing import List


def customSortString(order: str, str: str) -> str:
    # N * M * (M - N)

    res: List = []
    # use two pointers in order and str
    for i in order:
        for j in str:
            if i == j:
                res.append(i)

    # find out the remaining items and add them to res
    for i in str:
        if i not in order:
            res.append(i)

    return "".join(res)


customSortString("cba", "abcd")
