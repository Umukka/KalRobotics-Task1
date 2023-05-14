from typing import List

import time

from ultrasonic_sensor import DummyUltrasonicSensor, random_data_generator


class Robot:
    distance_threshold = 10
    average_distance: float = 0

    def navigate_robot(self):
        if self.average_distance < self.distance_threshold:
            return " Stop"
        else:
            return "Continue"

    def start(self):
        distance_list = []

        distance_sensor = DummyUltrasonicSensor(random_data_generator(0, 18))

        time_checkpoint = time.time()
        while True:
            if time.time() - time_checkpoint >= 10:
                current_distance = distance_sensor.get_distance()

                distance_list = [*distance_list[1:21], current_distance]

                time_checkpoint = time.time()

            self.average_distance = sum(distance_list) / len(distance_list)

            print(f'Average distance = {self.average_distance} | navigating robot >> {self.navigate_robot()}')
