import requests_mock
from component_1.main import fetch_data


def test_fetch_data():
    with requests_mock.Mocker() as m:
        m.get("http://test.com", json={"key": "value"})
        result = fetch_data("http://test.com")
        assert result == {"key": "value"}
