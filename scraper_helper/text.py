import re


def cleanup(s):
    if s:
        return re.sub('\n\r\t', '', s).strip()
    else:
        return None


def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            # v = kv.split(sep)[1]
            if strip_cookie and k == 'Cookie': continue
            if strip_cl and k == 'Content-Length': continue
            if k in strip_headers: continue
            d[k] = v
    return d
