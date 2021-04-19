import re


def get_clean_currency(param, keep_comma=False, keep_period=True):
    if not keep_comma and keep_period:
        pattren = r'[\d.]*'
    elif keep_comma and not keep_period:
        pattren = r'[\d,]*'
    else:
        pattren = r'[\d,.]*'

    result = re.search(pattren, param)
    if result:
        return result.group(0)
    else:
        return None


def cleanup(s):
    """ Takes a string and cleans it by removing newline, tab and whitespace.
    @param s: Any string
    @return: Cleaned up string
    """
    if s:
        r = re.sub('(\r\n)(\t)', ' ', s).strip()
        r = ' '.join([x for x in r.split()])
        if r:
            r = r.replace('\xa0', ' ')  # &nbsp to space
        return r
    else:
        return None


def get_headers(s: str, sep: str = ': ', strip_cookie: bool = True, strip_cl: bool = True,
                strip_headers: list = []) -> dict:
    """get_headers will be deprecated. Use get_dict instead
    """
    return get_dict(s, sep, strip_cookie, strip_cl, strip_headers)


def get_dict(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict:
    """Takes headers copied from dev tools and converts to string. Note that this consider each line
    as new dictionary key. Thus pass input as string in triple quotes.
    Example Input:
    '''
    accept: */*
    accept-encoding: gzip, deflate, br
    '''
    Example Output:
    {'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br'}
    @param s: Input string in triple quotes
    @param sep: The separator for key and value. Defaults to :
    @param strip_cookie: Remove cookies. Defaults to True
    @param strip_cl: Remove content-length: Defaults to True
    @param strip_headers: Optional list of keys that needs to be excluded
    @return: dictionary
    @rtype: dict
    """
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v = ''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if k[:1] == ":":
                continue
            if strip_cookie and k.lower() == 'cookie':
                continue
            if strip_cl and k.lower() == 'content-length':
                continue
            if k in strip_headers:
                continue
            d[k] = v
    return d


def headers(browser="chrome"):
    header_dictionary = {'accept': '*/*',
                         'accept-encoding': 'gzip, deflate, br',
                         'accept-language': 'en-US,en;q=0.9',
                         'cache-control': 'no-cache',
                         'pragma': 'no-cache',
                         'referer': 'https://www.google.com/',
                         'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                         'sec-ch-ua-mobile': '?0',
                         'sec-fetch-dest': 'empty',
                         'sec-fetch-mode': 'cors',
                         'sec-fetch-site': 'same-origin',
                         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    if browser.lower() == "chrome":
        return header_dictionary
    elif browser.lower() == "firefox":
        header_dictionary['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
        return header_dictionary
    else:
        return header_dictionary
