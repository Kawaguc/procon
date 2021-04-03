class RollingHash:
    def __init__(self, s, base=1007, mod=10 ** 9 + 7):
        """
        O(len(s))
        """
        self.mod = mod
        self.pows = [1] * (len(s) + 1)
        self.hashs = [0] * (len(s) + 1)
        for i in range(len(s)):
            self.hashs[i + 1] = (self.hashs[i] * base + ord(s[i])) % mod
            self.pows[i + 1] = self.pows[i] * base % mod

    def get(self, l, r):
        """
        returns hash of s[l:r) by O(1)
        """
        return (self.hashs[r] - self.hashs[l] * self.pows[r - l]) % self.mod


def main():
    # https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
    t = input()
    p = input()
    rh = RollingHash(t)
    hashp = RollingHash(p).get(0, len(p))
    for i in range(len(t) - len(p) + 1):
        if rh.get(i, i + len(p)) == hashp:
            print(i)


if __name__ == "__main__":
    main()
