from runner import Runner
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_obgect = Runner('Oleg')
        for i in range(10):
            test_obgect.walk()
        self.assertEqual(test_obgect.distance, 50)
    def test_run(self):
        test_obgect = Runner('Oleg')
        for i in range(10):
            test_obgect.run()
        print(test_obgect.distance)
        self.assertEqual(test_obgect.distance, 100)
    def test_challenge(self):
        walk = Runner('Ermak')
        run = Runner('Oleg')
        for i in range(10):
            walk.walk()
            run.run()
        self.assertNotEqual(walk.distance, run.distance)








