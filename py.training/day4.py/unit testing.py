
import unittest
class testsum(unittest.Testcase):

    def test_sum1(self):
        self.assertequal(sum([1,2,3]),6)

    def test_sum2(self):
        self.assertequal(sum([1,2,2]),5)
if __name__=="__main__":
    unittest.main()
