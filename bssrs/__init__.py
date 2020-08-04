# -*- coding: utf-8 -*-
"""
MIT License
===========

The bssrs/images dir and some source files under other terms (see NOTICE.txt).

Copyright (c) 2020- BSSRS Project Contributors and others (see AUTHORS.txt)

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

version_info = (0, 1, 0, "dev0")

__version__ = '.'.join(map(str, version_info))
__license__ = __doc__
__project_url__ = 'https://github.com/Maninder-mike/bant-shuttring-store-renting-system'
__forum_url__ = None
__trouble_url__ = __project_url__ + '/wiki/Troubleshooting-Guide-and-FAQ'
__trouble_url_short__ = None
__website_url__ = None

# following path to module's data (images) and translations:
DATAPATH = LOCALEPATH = DOCPATH = MATHJAXPATH = JQUERYPATH = ''

import os

# Directory of the current file
__dir__ = os.path.dirname(os.path.abspath(__file__))


def add_to_distribution(dist):
    """Add package to py2exe/cx_Freeze distribution object
    Extension to guidata.disthelpers"""
    try:
        dist.add_qt_bindings()
    except AttributeError:
        raise ImportError("This script requires guidata 1.5+")
    for _modname in ('bssrs', '_'):
        dist.add_module_data_files(_modname, ("",),
                                   ('.png', '.svg', '.html', '.png', '.txt',
                                    '.js', '.inv', '.ico', '.css', '.doctree',
                                    '.qm', '.py',),
                                   copy_to_root=False)


# TODO Correct vcs file here

def get_versions(reporev=True):
    """Get version information for components used by BSSRS"""
    import sys
    import platform

    import qtpy
    import qtpy.QtCore

    revision = None

    if not sys.platform == 'darwin':  # To avoid a crash with our Mac app
        system = platform.system()
    else:
        system = 'Darwin'

    return {
        'bssrs': __version__,
        'python': platform.python_version(),
        'bitness': 64 if sys.maxsize > 2 ** 32 else 32,
        'qt': qtpy.QtCore.__version__,
        'qt_api': qtpy.API_NAME,
        'qt_api_ver': qtpy.PYQT_VERSION,
        'system': system,
        'release': platform.release(),
        'revision': revision,
        'branch': branch,
    }
