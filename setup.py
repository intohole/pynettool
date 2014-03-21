from distutils.core import setup
import sys

kw = dict(
    name='pynettool',
    version='0.0.2',
    description='fast use web service ',
    author='intoblack',
    author_email='intoblack86@gmail.com',
    url='https://github.com/intoblack/pynettool',
    download_url='https://github.com/intoblack/pynettool',
    packages=['pynettool', 'pynettool/utils'],
    package_dir={'pynettool': 'pynettool'},
    package_data={'pynettool': ['data/*.txt']}
)

setup(**kw)
