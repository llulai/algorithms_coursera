# Uses python3
import sys

def gcd_naive(a, b):
    mayor = max(a, b)
    menor = min(a, b)
    rest = 1

    while rest > 0:
        rest = mayor % menor

        if rest == 0:
            return menor
        else:
            mayor, menor = menor, rest

    return rest

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
