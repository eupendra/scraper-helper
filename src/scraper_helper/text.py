import re


def cleanup(s):
    if s:
        r = re.sub('(\r\n)(\t)', ' ', s).strip()
        r = ' '.join([x for x in r.split()])
        print(f"Got ~{s}~ returning ~{r}~")
        return r
    else:
        return None


"""
get_headers will be deprecated. Use ```get_dict``` instead
"""


def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
    return get_dict(s, sep, strip_cookie, strip_cl, strip_headers)


def get_dict(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
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
            # v = kv.split(sep)[1]
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
