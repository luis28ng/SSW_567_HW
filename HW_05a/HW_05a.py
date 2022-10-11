from unittest import mock
from HW_04a.HW_04a import search_repo
import HW_04a.HW_04a


def use_search_repo():
    result = HW_04a.HW_04a.main()
    return result

use_search_repo()
# def repo_side_effect():
#     return "kaboow"
#
#
# @mock.patch('HW_04a.HW_04a.search_repo')
# def mock_search_repo(mock_repo):
#     mock_repo.return_value = 'this function is mocked'
#     result = HW_04a.HW_04a.search_repo()
#     print(result)
#
#
# @mock.patch('HW_04a.HW_04a.search_repo')
# def mock_search_repo_with_side_effect(mock_repo):
#     mock_repo.side_effect = repo_side_effect
#     result = HW_04a.HW_04a.search_repo()
#     print(result)
#
#
# mock_search_repo()
# mock_search_repo_with_side_effect()