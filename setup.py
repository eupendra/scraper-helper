import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scraper_helper", # Replace with your own username
    version="0.0.1",
    author="Upendra",
    author_email="upendra@coderecode.com",
    description="Helper functions for scraping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eupendra/scraper-helper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
