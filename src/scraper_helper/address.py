import logging
import re

from .text import cleanup


def get_zip(param,country='US'):
    logging.debug(f'Extracting Zip from {param}')
    if country.upper() == 'CA':
        return get_zip_CA(param)
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

def get_zip_CA(param):
    logging.debug(f'Extracting Canadian Zip from {param}')
    if param:
        result = re.search(r'[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d', param)
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
        zip_code = get_zip(param)
        param = param.replace(zip_code, '')
        param_parts = param.split(',')
        city = cleanup(param_parts[0])
        state = cleanup(param_parts[1])

        return (city, state, zip_code)
    except:
        return (param, None, None)

def SplitAddress_CA(param) -> tuple:
    """
    param address like 1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9
    Return Street, City, Province ZIP
    """
    try:
        zip_code = get_zip_CA(param)
        param = param.replace(zip_code, '').strip()
        param_parts = param.split(',')
        street = cleanup(param_parts[0])
        city = cleanup(param_parts[1])
        province = cleanup(param_parts[2])


        return (street, city, province, zip_code)
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
        if last_name:
            last_name = last_name.strip()
        if first_name:
            first_name = first_name.strip()
        return (first_name, last_name)


def extract_emails(s):
    pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return re.findall(pattern, s)
    
    
    