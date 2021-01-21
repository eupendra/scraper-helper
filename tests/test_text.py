from scraper_helper.text import cleanup
from scraper_helper.text import get_dict
from scraper_helper.text import get_headers


def test_cleanup():
    param = '''
        this\ris     a
            test
            '''
    expected = "this is a test"

    assert cleanup(param) == expected


def test_cleanup_error():
    param = None
    expected = None
    assert cleanup(param) == expected


def test_get_dict():
    param = '''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9
    cache-control: no-cache
    cookie: CTK=1ere641j5osgn801; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtbOFhsKDAt8twtbhyvY_Vos="
    pragma: no-cache
    sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
    sec-ch-ua-mobile: ?0
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: none
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    '''

    expected = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    assert get_dict(param) == expected


def test_get_headers():
    param = '''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9
    cache-control: no-cache
    cookie: CTK=1ere641j5osgn801; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtbOFhsKDAt8twtbhyvY_Vos="
    pragma: no-cache
    sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
    sec-ch-ua-mobile: ?0
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: none
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    '''

    expected = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    assert get_headers(param) == expected


def test_get_dict_strip_content_length_true():
    param = '''
    accept-encoding: gzip, deflate, br
    content-length:1025
    '''

    expected = {
        'accept-encoding': 'gzip, deflate, br',
    }

    assert get_dict(param) == expected


def test_get_dict_strip_content_strip_headers():
    param = '''
    accept-encoding: gzip, deflate, br
    sec-fetch-mode: 'navigate',
    sec-fetch-site: 'none',
    '''
    strip_headers = ['sec-fetch-mode', 'sec-fetch-site']
    expected = {
        'accept-encoding': 'gzip, deflate, br',
    }

    assert get_dict(param, strip_headers=strip_headers) == expected


def test_get_dict_ignore_colon():
    param = '''
    :authority: www.amazon.com
    :method: GET
    :path: /s?k=lens&i=photo&rh=n%3A499248%2Cp_89%3ATamron&dc&qid=1611208858&rnid=2528832011&ref=sr_nr_p_89_9
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9
    '''
    expected = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'
    }
    assert get_dict(param) == expected
