from timers import *


@time_function
def recursive_fib(n) -> int:
    def aux(n):
        if n <= 1:
            return n
        else:
            return aux(n - 1) + aux(n - 2)

    return aux(n)


@time_function_ns
def tail_recursive_fib(n) -> int:
    def aux(n, acc, p):
        if n == 0:
            return acc
        return aux(n - 1, acc + p, acc)

    return aux(n, 0, 1)


@time_function_ns
def non_recursive_fib(n) -> int:
    x = 0
    y = 1
    for _ in range(n):
        x, y = x + y, x
    return x


if __name__ == "__main__":
    assert recursive_fib(33) == tail_recursive_fib(33) == non_recursive_fib(33)
