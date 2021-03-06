from datetime import date, datetime


def decorator_parametrized_logger(filename='parametrized_logs.txt'):
    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            with open(file=filename, mode='a+', encoding='utf8') as log_file:
                log_file.write(f'Function "{func.__name__}" started at {date.today()} {datetime.now().time()}\n')
                log_file.write(f'Arguments is: {args}, {kwargs}\n')
                result = func(*args, **kwargs)
                log_file.write(f'Function "{func.__name__}" stopped at {date.today()} {datetime.now().time()}\n')
                log_file.write(f'Result is: {result}\n\n')
            return result
        return wrapper_func
    return decorator_func


def decorator_default_logger(old_function):
    def new_function(*args, **kwargs):
        with open(file='default_logs.txt', mode='a+', encoding='utf8') as log_file:
            log_file.write(f'Function "{old_function.__name__}" started at {date.today()} {datetime.now().time()}\n')
            log_file.write(f'Arguments is: {args}, {kwargs}\n')
            result = old_function(*args, **kwargs)
            log_file.write(f'Result is: {result}\n\n')
        return result
    return new_function