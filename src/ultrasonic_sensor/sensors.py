from typing import Generator

from .base import DistanceSensor

class DummyDistanceSensor(DistanceSensor):
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