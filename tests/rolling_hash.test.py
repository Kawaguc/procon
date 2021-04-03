# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
from procon.rolling_hash import RollingHash


def main():
    t = input()
    p = input()
    rh = RollingHash(t)
    hashp = RollingHash(p).get(0, len(p))
    for i in range(len(t) - len(p) + 1):
        if rh.get(i, i + len(p)) == hashp:
            print(i)


if __name__ == "__main__":
    main()
