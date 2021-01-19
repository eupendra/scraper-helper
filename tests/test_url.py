from scraper_helper.url import change_param
from scraper_helper.url import get_query_str_val
from scraper_helper.url import get_root_address
from scraper_helper.url import strip_qs_params


def test_change_param():
    param = "http://coderecode.com/?p=test"
    expected = "http://coderecode.com/?p=changed"

    assert change_param(param, "p", "changed") == expected


def test_get_query_str_val():
    param = "http://coderecode.com/?p=test"
    expected = "test"

    assert get_query_str_val(param, "p") == expected


def test_strip_qs_params():
    param = "http://coderecode.com/something?p=test"
    expected = "http://coderecode.com/something"

    assert strip_qs_params(param) == expected


def test_get_root_address():
    param = "http://coderecode.com/?p=test"
    expected = "http://coderecode.com"

    assert get_root_address(param) == expected
