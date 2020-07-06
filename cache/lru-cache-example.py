from functools import lru_cache
import urllib


@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except Exception:
        return 'Not Found'

# Example of efficiently computing Fibonacci numbers using a cache to implement a dynamic programming technique


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for n in [8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991]:
        pep = get_pep(n)
        print(n, len(pep))
    for i in range(200):
        print(fib(i))


if __name__ == '__main__':
    main()
