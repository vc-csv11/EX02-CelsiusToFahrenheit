import unittest
import subprocess
import re
import random
import xmlrunner

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

    def executeTest(self, c, expected, regex):
        # call hello world script command ##
        p = subprocess.Popen("python src/celsius_to_fahrenheit.py", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, bufsize=1)

        (output, err) = p.communicate('{0}'.format(c).encode())
        p_status = p.wait()

        m = re.search(regex, output.decode('utf-8'))
        self.assertEqual(expected, float(m.group(1)))
        CelsiusToFahrenheitTest.testScore += 4
        self.assertEqual(0, p_status)
        CelsiusToFahrenheitTest.testScore += (2 + 2/3)

    def testFrozen(self):
        self.executeTest(0, 32, "\D*(\d+).*\n$")

    def testBoiling(self):
        self.executeTest(100, 212, "\D*(\d+).*\n$")

    def testRandom(self):
        c = random.randint(-12, 200)
        self.executeTest(c, 9/5 * c + 32, '\D*(\d+(\.\d+)?).*\n$')


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
