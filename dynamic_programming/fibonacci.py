def fib(n):
    """
    Recursive relation
    + O(2^n)
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_dp_top_down(n, fib_vals = [1, 1]):
    """
    Memoization stores the result of expensive function calls (in arrays or objects),
    and returns the stored results
    + top-down approach, meaning we start with what we are trying to find
    + O(n)
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    if n < len(fib_vals):
        return fib_vals[n]
    result = fib_dp_top_down(n - 1, fib_vals) + fib_dp_top_down(n - 2, fib_vals)
    fib_vals.insert(n, result)
    return result


def fib_dp_btm_up(n, fib_vals = [1, 1]):
    """
    Tabulation is usually accomplished through iteration (a loop).
    Starting from the smallest subproblem, we store the results in a table (an array)
    + bottom-up approach, we start from the bottom, finding fib(0) and fib(1),
      add them together to get fib(2) and so on until we reach fib(5).
    + O(n)
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    for i in range(2, n+1):
        fib_vals.insert(i, fib_vals[i-1] + fib_vals[i-2])
    return fib_vals[n]

assert 1 == fib(0)
assert 1 == fib_dp_top_down(0)
assert 1 == fib_dp_btm_up(0)

assert 1 == fib(1)
assert 1 == fib_dp_top_down(1)
assert 1 == fib_dp_btm_up(1)

assert 2 == fib(2)
assert 2 == fib_dp_top_down(2)
assert 2 == fib_dp_btm_up(2)

assert 3 == fib(3)
assert 3 == fib_dp_top_down(3)
assert 3 == fib_dp_btm_up(3)

assert 5 == fib(4)
assert 5 == fib_dp_top_down(4)
assert 5 == fib_dp_btm_up(4)

assert 8 == fib(5)
assert 8 == fib_dp_top_down(5)
assert 8 == fib_dp_btm_up(5)

assert 8 == fib(5)
assert 8 == fib_dp_top_down(5)
assert 8 == fib_dp_btm_up(5)

assert 218922995834555169026 == fib(99)
assert 218922995834555169026 == fib_dp_top_down(99)
assert 218922995834555169026 == fib_dp_btm_up(99)
