import sys
from setuptools import setup

dev_requirements = ['pytest>=7.0', 'twine>=4.0.2']

if len(sys.argv) >= 2 and sys.argv[1] == 'print-dev-requirements':
    for dep in dev_requirements:
        print(dep)
else:
    setup(
        name='mypak',
        version='0.0.1',
        long_description='Sample Python package',
        long_description_content_type='text/markdown',
        package_dir={'': 'src'},
        install_requires=['shortid>=0.1.2'],
        extras_require={'dev': dev_requirements},
    )
