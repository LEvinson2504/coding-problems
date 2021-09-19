class Solve:
    points = 0

    def maximumGain(self, s: str, x: int, y: int) -> int:

        if "ab" in s:
            s = s.replace("ab", "", 1)
            self.points += x
            self.maximumGain(s, x, y)
        if "ba" in s:
            s = s.replace("ba", "", 1)
            self.points += y
            self.maximumGain(s, x, y)
        if "ab" and "ba" not in s:
            return self.points


a = Solve()
print(a.maximumGain(s="cdbcbbaaabab", x=4, y=5))
