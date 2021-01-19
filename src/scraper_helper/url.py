from urllib.parse import parse_qsl
from urllib.parse import urlencode
from urllib.parse import urlparse


def change_param(url, param, new_value, create_new=False, upgrade_https=False):
    if not url:
        raise ValueError("URL cannot be null")
    elif "?" in url:
        q = url.split("?")[1]
        d = dict(parse_qsl(q))
        d[f"{param}"] = new_value

        new_url = url.split("?")[0] + "?" + urlencode(d)

    elif create_new:
        return url + "?" + urlencode({param: new_value})
    else:
        return url
    if upgrade_https:
        return new_url.replace("http://", "https://")
    else:
        return new_url


def get_query_str_val(url, qs):
    if not url:
        raise ValueError("URL cannot be null")
    elif "?" in url:
        q = url.split("?")[1]
        d = dict(parse_qsl(q))
        return d.get(qs)


def strip_qs_params(url):
    if not url:
        raise ValueError("URL cannot be null")

    u = urlparse(url)
    return f"{u.scheme}://{u.netloc}{u.path}"


def get_root_address(url):
    if not url:
        raise ValueError("URL cannot be null")

    u = urlparse(url)
    return f"{u.scheme}://{u.netloc}"
