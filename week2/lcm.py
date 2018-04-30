# Uses python3
import sys
from time import sleep


def lcm_naive(a, b):
    mcm = 1
    i = 2

    while a > 1 or b > 1:

        while a % i == 0 or b % i == 0:
            mcm *= i

            if a % i == 0:
                a /= i
            if b % i == 0:
                b /= i
        i += 1

    return mcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

    # assert 1933053046 == lcm_naive(28851538, 1183019)
    # assert 24 == lcm_naive(6, 8)
