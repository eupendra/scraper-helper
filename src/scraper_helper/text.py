import re


def cleanup(s):
    """ Takes a string and cleans it by removing newline, tab and whitespace.
    @param s: Any string
    @return: Cleaned up string
    """
    if s:
        r = re.sub('(\r\n)(\t)', ' ', s).strip()
        r = ' '.join([x for x in r.split()])
        print(f"Got ~{s}~ returning ~{r}~")
        return r
    else:
        return None


def get_headers(s: str, sep: str = ': ', strip_cookie: bool = True, strip_cl: bool = True,
                strip_headers: list = []) -> dict:
    """get_headers will be deprecated. Use get_dict instead
    """
    return get_dict(s, sep, strip_cookie, strip_cl, strip_headers)


def get_dict(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
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
            if v == '\'\'':
                v = ''
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
