import unittest
from prefix import *
import io

class Testword(unittest.TestCase):
    def test_roman_numeral(self):
        self.assertEqual(find_prefix('filex.txt'),'gre')
        self.assertEqual(find_common_prefix(['ax', 'apple', 'book', 'banana'] ),'a')
        self.assertEqual(find_common_prefix(['app', 'apple', 'book', 'banana', 'cook', 'coat','common','compare', 'coated']),'co')
        self.assertEqual(find_common_prefix2(['ax', 'apple', 'book', 'banana'] ),'a')
        self.assertEqual(find_common_prefix2(['app', 'apple', 'book', 'banana', 'cook', 'coat','common','compare', 'coated']),'co')
    
    def testReadingOfInitialsFromFileStream(self):
        testStream = io.StringIO()
        testStream.write('grep\ngre\ngrenade \n')
        testStream.seek(0)
        self.assertEqual(['grep\n', 'gre\n', 'grenade \n'], readPrefixFromFileStream(testStream))

unittest.main()
