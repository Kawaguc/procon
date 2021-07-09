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
