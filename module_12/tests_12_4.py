import module_12_4
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s ~(>_<~) %(levelname)s ~(>_<~) %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_runner = module_12_4.Runner('test', -5)
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_runner = module_12_4.Runner(13)
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner_1 = module_12_4.Runner('test1')
        test_runner_2 = module_12_4.Runner('test2')
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
            self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


if __name__ == '__main':
    unittest.main()
