import unittest

class TestMagazine(unittest.TestCase):
    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")

if __name__ == '__main__':
    unittest.main()
