import unittest
from UnitTest import Art


class MyTestCase(unittest.TestCase):
    def test_add(self):
        sum=Art.add(10,20)


if __name__ == '__main__':
    unittest.main()
