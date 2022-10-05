from HW_04a import search_repo

import unittest


class TestRepo(unittest.TestCase):
    def test_repo_1(self):
        self.assertEqual(search_repo('richkempinski'), 9)

    def test_repo_2(self):
        self.assertEqual(search_repo('ldomadia'), 15)


if __name__ == '__main__':
    unittest.main()
