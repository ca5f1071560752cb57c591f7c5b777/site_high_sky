from setuptools import setup, find_packages
from os.path import join, dirname

classifiers = [
    'Environment :: Console',
    'License :: Public Domain',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Topic :: Web',
    ]

setup(
    name='site-high-sky',
    version='0.0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'Django',
        'django-rest-framework',
        'psycopg2-binary',
    ],
    entry_points={ },
)
