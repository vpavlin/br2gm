#!/usr/bin/env python

import re

from setuptools import setup, find_packages

def _get_requirements(path):
    try:
        with open(path) as f:
            packages = f.read().splitlines()
    except (IOError, OSError) as ex:
        raise RuntimeError("Can't open file with requirements: %s", repr(ex))
    packages = (p.strip() for p in packages if not re.match("^\s*#", p))
    packages = list(filter(None, packages))
    return packages

def _install_requirements():
    requirements = _get_requirements('requirements.txt')
    return requirements

setup(name='br2gm',
      version='0.1',
      description='Take a BBC Radio 1 Chart and make it a Google Music Playlist',
      author='Vaclav Pavlin',
      author_email='vaclav.pavlin@gmail.com',
      url='https://github.com/vpavlin/br2gm',
      license="MIT",
      entry_points={
          'console_scripts': ['br2gm=br2gm.cli.main:run'],
      },
      packages=find_packages(),
      install_requires=_install_requirements(),
)
