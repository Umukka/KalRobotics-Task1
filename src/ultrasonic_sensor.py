from typing import Generator

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


class DummyDistanceSensor:
    """A dummy distance sensor class to be used for testing.

    Attributes
    ----------
    data_stream: Generator[float, None, None]
        The data stream to generate distance data.
    """
    data_stream: Generator[float, None, None]

    def __init__(self, data_stream: Generator[float, None, None]):
        self.data_stream = data_stream

    def get_distance(self) -> float:
        return next(self.data_stream)
