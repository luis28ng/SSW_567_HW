import unittest

import HW_05a
from unittest import mock


class TestMockRepo(unittest.TestCase):

    @mock.patch('HW_05a.search_repo')
    def test_mock_search_repo(self, mock_repo):
        mock_repo.return_value = 1
        repo_amount = HW_05a.search_repo('luis28ng')
        self.assertEqual(1, repo_amount)

    @mock.patch('HW_05a.search_repo')
    def test_mock_search_repo2(self, mock_repo):
        mock_repo.return_value = 15
        repo_amount = HW_05a.search_repo('ldomadia')
        self.assertEqual(15, repo_amount)

    @mock.patch('HW_05a.search_repo')
    def test_mock_search_repo3(self, mock_repo):
        mock_repo.return_value = 9
        repo_amount = HW_05a.search_repo('richkempinski')
        self.assertEqual(9, repo_amount)
