import unittest
import subprocess
import re
import random


class CelsiusToFahrenheitTest(unittest.TestCase):
    testScore = 0

    MAX_TESTED_SCORE = 20
    MAX_OVERALL_SCORE = 25

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.testScore == cls.MAX_TESTED_SCORE:
            print("\nYour unit test score is ",
                  round(cls.testScore),
                  " out of ",
                  cls.MAX_TESTED_SCORE,
                  "\n")
        else:
            print("\nYour unit test score is ",
                  round(cls.testScore),
                  " out of ",
                  cls.MAX_TESTED_SCORE,
                  " (",
                  round(cls.testScore - cls.MAX_TESTED_SCORE),
                  ")\n")

        print("The assignment is worth a total of ",
              cls.MAX_OVERALL_SCORE,
              " where the remaining points")
        print("comes from grading related to documentation, algorithms, and other")
        print("criteria.\n\n")

    def executeTest(self, c, f):
        # call hello world script command ##
        p = subprocess.Popen("python3 ../src/celsius_to_fahrenheit.py", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, bufsize=1)

        (output, err) = p.communicate('{0}'.format(c).encode())
        p_status = p.wait()

        self.assertTrue(re.search(f, output.decode('utf-8')) is not None)
        CelsiusToFahrenheitTest.testScore += 4
        self.assertEqual(0, p_status)
        CelsiusToFahrenheitTest.testScore += (2 + 2/3)

    def testFrozen(self):
        self.executeTest(0, "\D*32.0\D?.*\n$")

    def testBoiling(self):
        self.executeTest(100, "\D*212.0\D?.*\n$")

    def testRandom(self):
        c = random.randint(-12, 200)
        self.executeTest(c, '\D*{0}.*\D?\n$'.format(9/5 * c + 32))


if __name__ == '__main__':
    unittest.main()
