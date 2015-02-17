from kata import Person

import unittest

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person()

    def test_init_with_clean_slate(self):
        self.assertEqual("Hello!", self.person.greet())

if __name__ == '__main__':
    unittest.main()
