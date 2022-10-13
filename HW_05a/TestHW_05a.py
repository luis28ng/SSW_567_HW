import unittest

import HW_05a
from unittest import mock


class TestMockRepo(unittest.TestCase):

    @mock.patch('HW_05a.search_repo')
    def test_mock_search_repo(self, mock_repo):
        mock_repo.return_value = 1
        repo_amount = HW_05a.search_repo('luis28ng')
        self.assertEqual(1, repo_amount)
