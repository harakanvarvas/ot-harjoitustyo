import unittest
from harjoitustyo import PracticeWork

class TestHarjoitustyo(unittest.TestCase):
    def setUp(self):
        self.work = PracticeWork()

    def test_created_work_exists(self):
        self.assertNotEqual(self.work, None)
