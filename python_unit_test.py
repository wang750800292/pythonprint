# encode: utf8
import unittest
class ClassName(unittest.TestCase):
    """docstring for ClassName"""
    def setUp(self):
        self.foo = 'foo'
        self.git = 'GIT'

    def tearDown(self):
        pass
    
    def test_upper(self):
        self.assertEqual(self.foo.upper(), 'FOO')

    def test_issupper(self):
        self.assertFalse(self.foo.isupper())
        self.assertTrue(self.git.isupper())

if __name__ == '__main__':
    unittest.main()

