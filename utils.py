from functools import wraps, update_wrapper


def memoize(func):
    memo = {}

    @wraps(func)
    def wrapper(*args):
        wrapper.called += 1
        if args in memo:
            wrapper.cache_hits += 1
            return memo[args]

        else:
            memo[args] = func(*args)
            wrapper.processed += 1
            return memo[args]

    wrapper.cache_hits = 0
    wrapper.processed = 0
    wrapper.called = 0

    return wrapper
