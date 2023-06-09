from typing import List

import time

from ultrasonic_sensor import DummyDistanceSensor, random_data_generator


class Robot:
    distance_threshold = 10
    average_distance: float = 0

    @classmethod
    def navigate_robot(cls, distance):
        if distance < cls.distance_threshold:
            return "Stop"
        else:
            return "Continue"

    def start(self):
        distance_list = []

        distance_sensor = DummyDistanceSensor(random_data_generator(0, 18))

        sensor_period_stamp = time.time()
        main_period_stamp = time.time()
        while True:
            if time.time() - sensor_period_stamp >= 0.1:
                current_distance = distance_sensor.get_distance()

                distance_list = [*distance_list[1:21], current_distance]

                sensor_period_stamp = time.time()

            if time.time() - main_period_stamp > 0.5:
                try:
                    self.average_distance = sum(
                        distance_list) / len(distance_list)
                except ZeroDivisionError:
                    self.average_distance = 0

                print(
                    f'Average distance = {self.average_distance} | navigating robot >> {self.navigate_robot(self.average_distance)}')

                main_period_stamp = time.time()
