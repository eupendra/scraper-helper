from scraper_helper.html import html_decode


def test_html_decode():
    param = "http://coderecode.com/?p=hd%20a%20[%20]%20#%204%205"
    expected = "http://coderecode.com/?p=hd a [ ] # 4 5"

    assert html_decode(param) == expected
