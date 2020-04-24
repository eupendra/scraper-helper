import logging
import re

from .text import cleanup


def get_zip(param):
    logging.debug(f'Extracting Zip from {param}')
    if param:
        result = re.search(r'[0-9]{5}(?:-[0-9]{4})?', param)
        if result:
            logging.debug(f'Got {result.group(0)}')
            return result.group(0)
        else:
            logging.warning(f'No match found for {param}in {result}')
            return None
    else:
        logging.warning('No zip found in None string')
        return None


def SplitAddress(param) -> tuple:
    """
    param address like San Diego, CA 92129 or San Francisco, CA 94105-5829
    Return City, State ZIP
    """
    try:
        zip = get_zip(param)
        param = param.replace(zip, '')
        param_parts = param.split(',')
        city = cleanup(param_parts[0])
        state = cleanup(param_parts[1])

        return (city, state, zip)
    except:
        return (param, None, None)


def SplitNames(param):

    # "Zijian Zhang , CPA, MSA, MSF"
    # "W Mills"#
    if param:
        name = cleanup(param)
        if ',' in name:
            name = name.split(',')[0]
        first_name = name.split(' ')[0]
        last_name = ' '.join(name.split(' ')[1:])
        return (first_name, last_name)


def extract_email_list(s):
    pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return re.findall(pattern, s)
    
    
    