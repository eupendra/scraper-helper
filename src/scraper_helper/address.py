import logging
import re

from .text import cleanup


def get_zip(address, country='US'):
    """

    @param address:
    @param country: Works only for US and CA. Defaults to US.
    @return: Zip Code string
    """
    logging.debug(f'Extracting Zip from {address}')
    if country.upper() == 'CA':
        return get_zip_canadian(address)
    if country.upper() not in ['CA', 'US']:
        raise ValueError("Only US and CA are supported.")
    if address:
        result = re.search(r'[0-9]{5}(?:-[0-9]{4})?', address)
        if result:
            logging.debug(f'Got {result.group(0)}')
            return result.group(0)
        else:
            logging.warning(f'No ZIP found for {address}in {result}')
            return None
    else:
        logging.warning('No zip found in None string')
        # Returning None instead of ValueError by design
        return None


def get_zip_canadian(address):
    """
    @param address: Canadian Address
    @return: Zip Codede
    """
    logging.debug(f'Extracting Canadian Zip from {address}')
    if address:
        result = re.search(r'[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d', address)
        if result:
            logging.debug(f'Got {result.group(0)}')
            return result.group(0)
        else:
            logging.warning(f'No match found for {address}in {result}')
            return None
    else:
        logging.warning('No zip found in None string')
        return None


def split_address(address) -> tuple:
    """
    @param address:
    @return:
    Splits address into US address into city, state, zip_code
    param address like San Diego, CA 92129 or San Francisco, CA 94105-5829
    Return City, State ZIP
    """
    try:
        zip_code = get_zip(address)
        address = address.replace(zip_code, '')
        param_parts = address.split(',')
        city = cleanup(param_parts[0])
        state = cleanup(param_parts[1])

        return city, state, zip_code
    except Exception as ex:
        logging.warning(f'Received error:\n{str(ex)}')
        return address, None, None


def split_address_canadian(address) -> tuple:
    """
    param address like 1776 Fourth Avenue, St. Catharines, Ontario L2R 6P9
    Return Street, City, Province ZIP
    @param address: Canadian Address
    @return: street, city, province, zip_code
    """
    try:
        zip_code = get_zip_canadian(address)
        address = address.replace(zip_code, '').strip()
        param_parts = address.split(',')
        street = cleanup(param_parts[0])
        city = cleanup(param_parts[1])
        province = cleanup(param_parts[2])

        return street, city, province, zip_code
    except Exception as ex:
        logging.warning(f'Received error:\n{str(ex)}')
        return address, None, None, None


def split_names(full_name):
    """
    Splits full name into fist name and last name
    Can accept names like "Zijian Zhang , CPA, MSA, MSF" and "W Mills"
    @param full_name: Full name string
    @return: first_name, last_name

    """
    if full_name:
        name = cleanup(full_name)
        if ',' in name:
            name = name.split(',')[0]
        first_name = name.split(' ')[0]
        last_name = ' '.join(name.split(' ')[1:])
        if last_name:
            last_name = last_name.strip()
        if first_name:
            first_name = first_name.strip()
        return first_name, last_name
    else:
        return "", ""


def extract_emails(s) -> list:
    """Accepts a string and returns a list of email addresses inside it
    @param s: Any string
    @return: list of email addresses
    """
    pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+" \
              r"(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)" \
              r"+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return re.findall(pattern, s)
