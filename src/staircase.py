# builds a staircase.
def staircase(n):
    if n in range(1, 101):
        for num in range(1, n+1):
            print(("#" * num).rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
