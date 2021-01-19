========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/scraper-helper/badge/?style=flat
    :target: https://readthedocs.org/projects/scraper-helper
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/eupendra/scraper-helper.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/eupendra/scraper-helper

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/eupendra/scraper-helper?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/eupendra/scraper-helper

.. |codecov| image:: https://codecov.io/gh/eupendra/scraper-helper/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/eupendra/scraper-helper

.. |version| image:: https://img.shields.io/pypi/v/scraper-helper.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/scraper-helper

.. |wheel| image:: https://img.shields.io/pypi/wheel/scraper-helper.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/scraper-helper

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/scraper-helper.svg
    :alt: Supported versions
    :target: https://pypi.org/project/scraper-helper

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/scraper-helper.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/scraper-helper

.. |commits-since| image:: https://img.shields.io/github/commits-since/eupendra/scraper-helper/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/eupendra/scraper-helper/compare/v0.0.2...master



.. end-badges

Helper functions for web scraping

* Free software: GNU GENERAL PUBLIC LICENSE

Installation
============

::

    pip install scraper-helper

You can also install the in-development version with::

    pip install https://github.com/eupendra/scraper-helper/archive/master.zip


Documentation
=============


https://scraper-helper.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
