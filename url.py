import logging


def change_param(url, param, new_value, create_new=False, upgrade_https=True):
    logging.info(f'Received {url}, {param}, {new_value}, {create_new}')
    try:
        from urllib.parse import parse_qsl, urlencode

        # url = 'https://www.calcpa.org/customsearchproxy/?mpp=72&ajax=1&json=1&lpurl=%2Fmembers-directory&hawkvisitorid=9e033e99-d972-4559-8888-25918c77235d&callback=jQuery31108884423299105249_1583380756978&_=1583380756986'
        if url is None:
            return None
        elif '?' in url:
            q = url.split('?')[1]
            d = dict(parse_qsl(q))
            d[f'{param}'] = new_value

            new_url = url.split('?')[0] + '?' + urlencode(d)
            if upgrade_https:
                return new_url.replace('http://', 'https://')
            else:
                return new_url
        elif create_new:
            return url + '?' + urlencode({param: new_value})
    except:
        print(f'Error in change param for {url}')
        return url


def get_query_str_val(url, qs):
    from urllib.parse import parse_qsl
    if url is None:
        return None
    elif '?' in url:
        q = url.split('?')[1]
        d = dict(parse_qsl(q))
        return d.get(qs)