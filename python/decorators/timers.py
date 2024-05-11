import time


def time_function(fn):
    def closure(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function took {end - start}s to complete")
        return result

    return closure


def time_function_ns(fn):
    def closure(*args, **kwargs):
        start = time.perf_counter_ns()
        result = fn(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f"Function took {end - start}ns to complete")
        return result

    return closure
