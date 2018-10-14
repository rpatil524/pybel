# -*- coding: utf-8 -*-

"""Setup.py for PyBEL."""

import codecs  # To use a consistent encoding
import os
import re
import sys

import setuptools

#################################################################

PACKAGES = setuptools.find_packages(where='src')
META_PATH = os.path.join('src', 'pybel', '__init__.py')
KEYWORDS = ['Biological Expression Language', 'BEL', 'Systems Biology', 'Networks Biology']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering :: Bio-Informatics'
]
INSTALL_REQUIRES = [
    'networkx>=2.1',
    'sqlalchemy',
    'click',
    'click-plugins',
    'requests',
    'requests_file',
    'pyparsing',
    'six',
    'tqdm',
    'configparser; python_version < "3"',
    'functools32; python_version < "3"',
    'funcsigs; python_version < "3"',
]

EXTRAS_REQUIRE = {
    'indra': ['indra'],
    'neo4j': ['py2neo==3.1.2'],
    'docs': [
        'sphinx-click',
    ],
}
TESTS_REQUIRE = [
    'mock',
    'pathlib',
]
ENTRY_POINTS = {
    'console_scripts': [
        'pybel = pybel.cli:main',
    ],
    'pybel.object_importer': [
        'nodelink = pybel.io:from_json',
        'bytes = pybel.io:from_bytes',
        'bel = pybel:from_path',
    ],
    'pybel.file_importer': [
        'nodelink = pybel.io:from_json_file',
        'bytes = pybel.io:from_pickle',
        'bel = pybel:from_lines',
    ],
    'pybel.object_exporter': [
        'nodelink = pybel.io:to_json',
        'bytes = pybel.io:to_bytes',
        'bel = pybel.canonicalize:to_bel_lines',
    ],
    'pybel.file_exporter': [
        'nodelink = pybel.io:to_json_file',
        'bytes = pybel.io:to_pickle',
        'bel = pybel.canonicalize:to_bel',
    ],
}
DEPENDENCY_LINKS = [
]

#################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Build an absolute path from *parts* and return the contents of the resulting file. Assume UTF-8 encoding."""
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """Extract __*meta*__ from META_FILE."""
    meta_match = re.search(
        r'^__{meta}__ = ["\']([^"\']*)["\']'.format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string'.format(meta=meta))


def get_long_description():
    """Get the long_description from the README.rst file. Assume UTF-8 encoding."""
    with codecs.open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


if __name__ == '__main__':
    setuptools.setup(
        name=find_meta('title'),
        version=find_meta('version'),
        description=find_meta('description'),
        long_description=get_long_description(),
        url=find_meta('url'),
        author=find_meta('author'),
        author_email=find_meta('email'),
        maintainer=find_meta('author'),
        maintainer_email=find_meta('email'),
        license=find_meta('license'),
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        packages=PACKAGES,
        package_dir={'': 'src'},
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        tests_require=TESTS_REQUIRE,
        entry_points=ENTRY_POINTS,
        dependency_links=DEPENDENCY_LINKS,
        zip_safe=False,
    )
