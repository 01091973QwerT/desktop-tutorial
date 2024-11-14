import unittest
import logging
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

logging.basicConfig(
    filename='runner_tests.log',
    filemode='w',
    level=logging.INFO,
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Speedy", -10)  # Передаем отрицательное значение
            for _ in range(5):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:  # Укажите нужный тип исключения
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем неверный тип
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:  # Укажите нужный тип исключения
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
