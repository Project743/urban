import module_12_2
import unittest

class TournamentTest(unittest.TestCase):
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


    def test_turnament_1vs3(self):
        turnament = module_12_2.Tournament(90, self.runner_1, self.runner_3)
        res = turnament.start()
        self.all_results['1vs3'] = {x:str(v) for x,v in res.items()}
        self.assertTrue(res[max(res.keys())] == 'Ник')


    def test_turnament_2vs3(self):
        turnament = module_12_2.Tournament(90, self.runner_2, self.runner_3)
        res = turnament.start()
        self.all_results['2vs3'] = {x: str(v) for x, v in res.items()}
        self.assertTrue(res[max(res.keys())] == 'Ник')

    def test_turnament_2vs1vs3(self):
        turnament = module_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = turnament.start()
        self.all_results['2vs1vs3'] = {x: str(v) for x, v in res.items()}
        self.assertTrue(res[max(res.keys())] == 'Ник')


    def test_turnament_valid_vin(self):
        turnament = module_12_2.Tournament(90, self.runner_2, self.runner_3, self.runner_1)
        res = turnament.start()
        self.assertTrue(res[min(res.keys())] == 'Усэйн')



if __name__ == '__main':
    unittest.main()