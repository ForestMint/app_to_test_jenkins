



import unittest
from script import convert_decimal_to_digital

'''
print(convert_decimal_to_digital(0))
print(convert_decimal_to_digital(1))
print(convert_decimal_to_digital(2))
'''

class TestConverter(unittest.TestCase):
    def test_add(self):
        self.assertEqual(convert_decimal_to_digital(0), "00000000")
        self.assertEqual(convert_decimal_to_digital(1), "00000001")
        self.assertEqual(convert_decimal_to_digital(4), "00000100")
        self.assertEqual(convert_decimal_to_digital(128), "10000000")
        self.assertEqual(convert_decimal_to_digital(255), "11111111")



if __name__ == '__main__':
    unittest.main()