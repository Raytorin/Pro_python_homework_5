from datetime import datetime


def logger(old_function):
    with open('task_3.log', 'w') as clear_file:
        pass

    def new_function(*args, **kwargs):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        title = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('task_3.log', 'a') as log_file:
            log_file.write(f'Дата вызова: {now}; Название: {title}; Аргументы: {args} и {kwargs}; Результат: {result}\n')
            return result
    return new_function
