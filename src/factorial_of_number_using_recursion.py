import math
import os
import random
import re
import sys


def factorial(n):
    if 2 <= n <= 12:
        rslt = fact(n)
        return rslt


def fact(m):
        if m <= 1:
            return 1
        else:
            return m * fact(m - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input())

    result = factorial(num)

    fptr.write(str(result) + '\n')

    fptr.close()



