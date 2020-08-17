def html_decode(s):
         htmlCodes = (
                     ("'", '&#39;'),
                     ('"', '&quot;'),
                     ('>', '&gt;'),
                     ('<', '&lt;'),
                     ('&', '&amp;'),
                     ('%20', ' '),
                     ('%22', '"'),
                     ('%2C', ','),
                     ('%3A', ':'),
                     ('%3C', '<'),
                     (r'%3E', '>')
        )
     for code in htmlCodes:
             s = s.replace(code[0], code[1])
     return s
