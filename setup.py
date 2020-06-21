from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='BSSRS',
    version='0.1.0',
    description='A POS Python project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maninder-mike',
    author='@maninder_mike',
    author_email='maninder.singh@outlook.in',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='sample setuptools development',

    package_dir={'': 'BSSRS'},  # Optional

    packages=find_packages(where='BSSRS'),

    python_requires='>=3.7, <4',

    install_requires=[
        'pyqt5'
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest'],
    },

    package_data={  # Optional
        'sample': ['package_data.dat'],
    },

    data_files=[('my_data', ['data/data_file'])],  # Optional

    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },

    project_urls={
        # 'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        # 'Source': 'https://github.com/pypa/sampleproject/',
    },
)
