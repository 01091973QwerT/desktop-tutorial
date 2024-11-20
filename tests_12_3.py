import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,"Тесты замороженны")

    def test_walk(self):
        runner = Runner("Тестер")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    @unittest.skipIf(is_frozen, "Тесты замороженны")
    def test_run(self):
        runner = Runner("Тестер")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты замороженны")
    def test_challenge(self):
        runner1 = Runner("Тестер 1")
        runner2 = Runner("Тестер 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты замороженны")
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, result in enumerate(cls.all_results):
            print(f"{i + 1}: {result}")

    @unittest.skipIf(is_frozen, "Тесты замороженны")
    def test_usain_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(
            self.all_results[len(self.all_results)].get(max(self.all_results[len(self.all_results)])) == "Ник")

    @unittest.skipIf(is_frozen, "Тесты замороженны")
    def test_andrey_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(
            self.all_results[len(self.all_results)].get(max(self.all_results[len(self.all_results)])) == "Ник")

    @unittest.skipIf(is_frozen, "Тесты замороженны")
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(
            self.all_results[len(self.all_results)].get(max(self.all_results[len(self.all_results)])) == "Ник")
