import unittest

from mypak import funk
from mypak.sub import bass


class SomeTest(unittest.TestCase):
    def test_funk(self) -> None:
        self.assertEqual(funk(), 'funk 1')

    def test_generate(self) -> None:
        self.assertTrue(bass())


if __name__ == '__main__':
    unittest.main()
