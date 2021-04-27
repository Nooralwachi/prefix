import unittest
from prefix import *

class Testword(unittest.TestCase):
    def test_roman_numeral(self):
        self.assertEqual(find_prefix('filex.txt'),'gre')
        self.assertEqual(find_common_prefix(['ax', 'apple', 'book', 'banana'] ),'a')
        self.assertEqual(find_common_prefix(['app', 'apple', 'book', 'banana', 'cook', 'coat','common','compare', 'coated']),'co')
        self.assertEqual(find_common_prefix2(['ax', 'apple', 'book', 'banana'] ),'a')
        self.assertEqual(find_common_prefix2(['app', 'apple', 'book', 'banana', 'cook', 'coat','common','compare', 'coated']),'co')
        
unittest.main()


