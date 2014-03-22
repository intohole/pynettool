import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

kw = dict(
    name='pynettool',
    version='0.0.3',
    description='fast use web service ',
    author='intoblack',
    author_email='intoblack86@gmail.com',
    url='https://github.com/intoblack/pynettool',
    download_url='https://github.com/intoblack/pynettool',
    packages=find_packages(),
    include_package_data=True
)

setup(**kw)
