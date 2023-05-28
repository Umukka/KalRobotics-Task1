from abc import ABC, abstractmethod

class DistanceSensor(ABC):
    @abstractmethod
    def get_distance(self) -> float: ...
