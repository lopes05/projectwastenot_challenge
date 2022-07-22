def humanize_time(total_seconds: float) -> str:
    return_str = ""
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    total_seconds = total_seconds % 60
    total_miliseconds = total_seconds * 1000 % 1000
    total_microseconds = total_seconds * 100000 % 1000
    return_str = "%d hours, %d minutes, %d seconds, %d miliseconds, %d microseconds" % (total_hours, total_minutes, total_seconds, total_miliseconds, total_microseconds)

    return return_str

def time_this_function(function: callable) -> callable:
    def wrapper(*args, **kwargs) -> callable:
        import time
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} took {end - start} seconds")
        print(humanize_time(end - start))
        return result
    return wrapper


@time_this_function
def range_sum(a: int, b: int) -> int:
    return sum(range(a, b))

if __name__ == '__main__':
    range_sum(int(input("Insira o primeiro número: ")), int(input("Insira o segundo número: ")))
