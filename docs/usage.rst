=====
Usage
=====

To install Scraper Helper in a project::

	import scraper_helper

The individual functions can then be imported and used:

    >>> from scraper_helper import extract_emails
    >>> text:str = "This string contains two mails - dell@email.com and hp@email.com"
    >>> emails = extract_emails(text)
    >>> print(emails)
    ['dell@email.com', 'hp@email.com']
