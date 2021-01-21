from urllib.parse import parse_qsl
from urllib.parse import urlencode
from urllib.parse import urlparse


def change_param(url, param, new_value, create_new=False, upgrade_https=False):
    """ Takes a url and changes the value of a query string parameter.
    @param url: The input url
    @param param: The name of the query string parameter that needs to be change
    @param new_value: The new value for the parameter
    @param create_new: If set to True, will create a new query string parameter
    @param upgrade_https: If set to true, will upgrade to HTTPS
    @return: Updated URL
    """
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


def get_query_str_val(url: str, qs: str) -> str:
    """Takes a url and extract value of a query string parameter.
    @rtype: str
    """
    if not url:
        raise ValueError("URL cannot be null")
    elif "?" in url:
        q = url.split("?")[1]
        d = dict(parse_qsl(q))
        return d.get(qs)


def strip_qs_params(url):
    """Takes a url and strips all query string parameters.
    @param url: Any url like https://coderecode.com/scrapy-crash-course?src=yt
    @return: full url without parameters: https://coderecode.com/scrapy-crash-course
    """
    if not url:
        raise ValueError("URL cannot be null")

    u = urlparse(url)
    return f"{u.scheme}://{u.netloc}{u.path}"


def get_root_address(url):
    """Takes a url and strips returns the root url
    @param url: Any url like https://coderecode.com/scrapy-crash-course?src=yt
    @return: full url without parameters: https://coderecode.com/
    """
    if not url:
        raise ValueError("URL cannot be null")

    u = urlparse(url)
    return f"{u.scheme}://{u.netloc}"
