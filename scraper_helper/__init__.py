__version__ = '0.0.1'
__all__ = [
    'address', 'text', 'url','cleanup', 'get_headers', 'get_zip', 'SplitAddress', 'SplitNames', 'extract_emails',
    'change_param','get_query_str_val','strip_qs_params','get_root_address'
]

__author__ = 'Upendra <eupendrajunk@gmail.com>'


from .address import *
from .text import *
from .url import *