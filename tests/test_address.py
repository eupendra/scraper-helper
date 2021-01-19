from scraper_helper.address import get_zip, get_zip_canadian, split_address, split_address_canadian
from scraper_helper.address import split_names, extract_emails


def test_get_zip():
    assert get_zip("San Diego, CA 92129") == "92129"


def test_get_zip_canadian():
    address = "1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert get_zip_canadian(address) == "L2R 6P9"


def test_split_address():
    address = "San Diego, CA 92129"
    assert split_address(address) == ("San Diego", "CA", "92129")


def test_split_address_canadian():
    address = "1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert split_address_canadian(address) == ("1776 Fourth Avenue", "St. Catharines", "Ontario", "L2R 6P9")


def test_split_names():
    name = "Zijian Zhang , CPA, MSA, MSF"
    assert split_names(name) == ("Zijian", "Zhang")


def test_extract_emails():
    param = "this is a test with email@address.com"
    assert extract_emails(param) == ["email@address.com"]
