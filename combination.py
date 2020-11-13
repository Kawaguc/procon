class Combination:
    """
    init:O(n) ex: c = Combination()
    call:O(1) ex: c(4,2) return 4C2 = 6
    """

    def __init__(self, n_max=1000000, mod=10 ** 9 + 7):
        """
        O(n)
        """
        self.mod = mod
        self.fac = [0] * (n_max + 1)
        self.facinv = [0] * (n_max + 1)
        self.inv = [0] * (n_max + 1)
        self.fac[0] = self.fac[1] = 1
        self.facinv[0] = self.facinv[1] = 1
        self.inv[1] = 1
        for i in range(2, n_max + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.mod // i * self.inv[self.mod % i] % self.mod
            self.facinv[i] = self.facinv[i - 1] * self.inv[i] % self.mod

    def __call__(self, n, r):
        """
        O(1)
        """
        if n < r or n < 0 or r < 0:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod


def main():
    pass


if __name__ == "__main__":
    main()
