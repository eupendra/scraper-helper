import re


def cleanup(param):
    if param:
        return re.sub('\n\r\t', '', param).strip()
    else:
        return None