import unittest


class ISimpleTest(unittest.TestCase):
    def setUp(self):
        self.msg = "hello world, simple test"

    def test_simple(self):
        print(f"Passing test {self.msg}")
        return self.assertEquals(self.msg, "hello world, simple test")


if __name__ == "__main__":
    unittest.main()
