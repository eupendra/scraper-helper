import pytest

from scraper_helper.address import extract_emails
from scraper_helper.address import get_zip
from scraper_helper.address import get_zip_canadian
from scraper_helper.address import split_address
from scraper_helper.address import split_address_canadian
from scraper_helper.address import split_names


def test_get_zip():
    assert get_zip("San Diego, CA 92129") == "92129"


def test_get_zip_no_zip():
    assert get_zip("San Diego, CA") is None


def test_get_zip_none_gets_none():
    assert get_zip(None) is None


def test_get_zip_canadian():
    address = "1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert get_zip_canadian(address) == "L2R 6P9"


def test_get_zip_with_country_ca():
    address = "1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert get_zip(address, country='CA') == "L2R 6P9"


def test_get_zip_error_country():
    address = "1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    country = "IN"
    with pytest.raises(ValueError):
        get_zip(address, country=country)


def test_split_address():
    address = "San Diego, CA 92129"
    assert split_address(address) == ("San Diego", "CA", "92129")


def test_split_address_number():
    address = 123
    assert split_address(address) == (123, None, None)


def test_split_address_invalid_type_dict():
    address = dict()
    assert split_address(address) == (dict(), None, None)


def test_split_address_invalid_type_exception():
    address = Exception
    assert split_address(address) == (Exception, None, None)


def test_split_address_canadian():
    address = "1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert split_address_canadian(address) == ("1776 Fourth Avenue", "St. Catharines", "Ontario", "L2R 6P9")


def test_split_address_canadian_cause_exception():
    address = Exception
    assert split_address_canadian(address) == (address, None, None, None)


def test_split_names_with_suffix():
    name = "Zijian Zhang , CPA, MSA, MSF"
    assert split_names(name) == ("Zijian", "Zhang")


def test_split_names_first_name_only():
    name = "Zijian"
    assert split_names(name) == ("Zijian", "")


def test_split_names_blank():
    name = None
    assert split_names(name) == ("", "")


def test_extract_emails():
    param = "this is a test with email@address.com"
    assert extract_emails(param) == ["email@address.com"]
