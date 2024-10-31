from setuptools import setup

setup(
    name='mypak',
    version='0.0.1',
    long_description='Sample Python package',
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    install_requires=['shortid>=0.1.2'],
    extras_require={'dev': ['pytest>=7.0', 'twine>=4.0.2']},
)
