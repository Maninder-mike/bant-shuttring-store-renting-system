from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='bssrs',
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

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'': 'src'},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where='src'),

    python_requires='>=3.7, <4',

    install_requires=[
        'pyqt5'
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        'sample': ['package_data.dat'],
    },

    data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
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
