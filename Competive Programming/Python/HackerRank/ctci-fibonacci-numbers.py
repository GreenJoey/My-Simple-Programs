def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 0

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n  = int(input())
    print(fibonacci(n))
