def mergeAlternately(word1: str, word2: str) -> str:
    l1, l2 = len(word1), len(word2)
    n: int = max(l1, l2)
    ans: str = ""
    for i in range(n):
        if i < l1:
            ans += word1[i]
        if i < l2:
            ans += word2[i]
    return ans


print(mergeAlternately("hello", "ben"))
