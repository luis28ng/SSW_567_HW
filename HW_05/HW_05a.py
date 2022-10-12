import json
from unittest import mock

import requests

import HW_04a.HW_04a
from HW_04a.HW_04a import search_repo


@mock.patch('request.get')
def mock_repo_counter(mock_request):
    mock_request.return_value = HW_04a.HW_04a.search_repo()
    result = HW_04a.HW_04a.main()
    print(result)


mock_repo_counter()
