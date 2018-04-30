# Uses python3
def calc_fib(n):
    start = [1, 1]
    if n > 1:
        for i in range(n-2):
            start.append(start[-1] + start[-2])

    print(start)

    return start[-1]

#n = int(input())
#print(calc_fib(n))

if __name__ == '__main__':
    print(calc_fib(10))