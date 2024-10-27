import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self, distance):
        self.distance += distance * self.speed

    def walk(self, distance):
        self.distance += distance / self.speed

class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for i, runner in enumerate(self.runners):
            runner.run(self.distance)
            results[i+1] = runner.name
        return results

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, result in enumerate(cls.all_results.values()):
            print(f"{i+1}: {result}")

    def test_usain_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        self.all_results[len(self.all_results)+1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)].get(max(self.all_results[len(self.all_results)])) == "Ник")

    def test_andrey_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        self.all_results[len(self.all_results)+1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)].get(max(self.all_results[len(self.all_results)])) == "Ник")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        self.all_results[len(self.all_results)+1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)].get(max(self.all_results[len(self.all_results)])) == "Ник")

if __name__ == '__main__':
    unittest.main()