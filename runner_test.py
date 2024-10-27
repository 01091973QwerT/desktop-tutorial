import unittest
from runner import Runner  # Импортируйте класс Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Тестер")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Тестер")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Тестер 1")
        runner2 = Runner("Тестер 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()