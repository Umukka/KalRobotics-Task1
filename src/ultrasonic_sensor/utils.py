import random

def random_data_generator(start: float, end: float) -> float:
    while True:
        yield random.uniform(start, end)


def file_data_generator(file_path: str) -> float:
    with open(file_path) as file:
        for i, line in enumerate(file.readlines()):
            try:
                yield float(line)
            except ValueError:
                raise ValueError(f"Invalid Line! >> {i+1}")