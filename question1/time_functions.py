def humanize_time(total_seconds: float) -> str:
    return_str = ""
    ONE_HOUR_IN_SECONDS = 3600
    ONE_MINUTE_IN_SECONDS = 60
    ONE_SECOND_IN_MILLISECONDS = 1000
    ONE_SECOND_IN_MICRO_SECONDS = 1000000

    MAX_SECONDS = 60
    MAX_MILISECONDS = 1000
    MAX_MICRO_SECONDS = 1000000

    total_hours = total_seconds // ONE_HOUR_IN_SECONDS
    total_minutes = (total_seconds % ONE_HOUR_IN_SECONDS) // ONE_MINUTE_IN_SECONDS
    total_seconds = total_seconds % MAX_SECONDS
    total_milliseconds = total_seconds * ONE_SECOND_IN_MILLISECONDS % MAX_MILISECONDS
    total_microseconds = total_seconds * ONE_SECOND_IN_MICRO_SECONDS % MAX_MICRO_SECONDS

    return_str = "%d hours, %d minutes, %d seconds, %d milliseconds, %d microseconds" % (total_hours, total_minutes, total_seconds, total_milliseconds, total_microseconds)
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
    range_sum(int(input("Insert first number: ")), int(input("Insert second number: ")))
