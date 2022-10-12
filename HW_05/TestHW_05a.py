from HW_04a.HW_04a import search_repo
from unittest import mock
import unittest



class TestMockRepo(unittest.TestCase):
    @mock.patch('HW_04a.HW_04a.request.get')
    def test_mock_repo(self, mock_repo):
        mock_repo.return_value.repo = '1'
        response = search_repo('luis28ng')

        self.assertEqual(response.repo, '1')


if __name__ == '__main__':
    unittest.main()
