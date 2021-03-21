# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A

from procon.prime_factorization import prime_factorization


def main():
    n = int(input())
    l = prime_factorization(n)
    sl = map(str, l)
    ret = str(n) + ": " + " ".join(sl)
    print(ret)


if __name__ == "__main__":
    main()
