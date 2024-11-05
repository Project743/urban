import module_12_2
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = module_12_2.Runner('Усэйн', 10)
        self.runner_2 = module_12_2.Runner('Андрей', 9)
        self.runner_3 = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turnament_1vs3(self):
        turnament = module_12_2.Tournament(90, self.runner_1, self.runner_3)
        res = turnament.start()
        self.all_results['1vs3'] = {x: str(v) for x, v in res.items()}
        self.assertTrue(res[max(res.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turnament_2vs3(self):
        turnament = module_12_2.Tournament(90, self.runner_2, self.runner_3)
        res = turnament.start()
        self.all_results['2vs3'] = {x: str(v) for x, v in res.items()}
        self.assertTrue(res[max(res.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turnament_2vs1vs3(self):
        turnament = module_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = turnament.start()
        self.all_results['2vs1vs3'] = {x: str(v) for x, v in res.items()}
        self.assertTrue(res[max(res.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turnament_valid_vin(self):
        turnament = module_12_2.Tournament(90, self.runner_2, self.runner_3, self.runner_1)
        res = turnament.start()
        self.assertTrue(res[min(res.keys())] == 'Усэйн')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_runner = module_12_2.Runner('test')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_runner = module_12_2.Runner('test')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner_1 = module_12_2.Runner('test1')
        test_runner_2 = module_12_2.Runner('test2')
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
            self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


if __name__ == '__main':
    unittest.main()
