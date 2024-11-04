import module_12_1
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = module_12_1.Runner('test')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = module_12_1.Runner('test')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)



    def test_challenge(self):
        test_runner_1 = module_12_1.Runner('test1')
        test_runner_2 = module_12_1.Runner('test2')
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
            self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


if __name__ == '__main__':
    unittest.main()