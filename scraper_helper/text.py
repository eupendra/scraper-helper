import re


def cleanup(s):
    if s:
        return re.sub('\n\r\t', '', s).strip()
    else:
        return None


def get_headers(s, sep=': ', strip_cookie=True,strip_cl=True, strip_headers:list=[]) -> dict():
    d = dict()
    for kv in s.split('\n'):
        if kv and sep in kv:
            if len(kv.split(sep)) == 1:
                k = kv.split(sep)[0]
                v = ''
            v = kv.split(sep)[1]
            if strip_cookie and k == 'cookie': continue
            if strip_cl and k == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d
