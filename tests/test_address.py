from scraper_helper.address import *


def test_get_zip():
    assert get_zip("San Diego, CA 92129") == "92129"

def test_get_zip_CA():
    address="1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert get_zip_CA(address) == "L2R 6P9"
def test_SplitAddress():
    address="San Diego, CA 92129"
    assert SplitAddress(address) == ("San Diego", "CA", "92129")
    
def test_SplitAddress_CA():
    address="1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9"
    assert SplitAddress_CA(address) == ("1776 Fourth Avenue", "St. Catharines", "Ontario", "L2R 6P9")

def test_SplitNames():
    name="Zijian Zhang , CPA, MSA, MSF"
    assert SplitNames(name)==("Zijian", "Zhang")


def test_extract_emails():
    param="this is a test with email@address.com"
    assert extract_emails(param) == ["email@address.com"]

# def extract_emails(s):
#     pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
#     return re.findall(pattern, s)
