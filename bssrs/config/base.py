from __future__ import print_function

import os
import os.path as osp
import re
import sys

# Local imports
from bssrs import __version__

DEV = os.environ.get('SPYDER_DEV')

USE_DEV_CONFIG_DIR = os.environ.get('SPYDER_USE_DEV_CONFIG_DIR')

SAFE_MODE = os.environ.get('SPYDER_SAFE_MODE')


def running_under_pytest():
    return bool(os.environ.get('SPYDER_PYTEST'))


def is_stable_version(version):
    if not isinstance(version, tuple):
        version = version.split('.')
    last_part = version[-1]

    if not re.search(r'[a-zA-Z]', last_part):
        return True
    else:
        return False


def use_dev_config_dir(use_dev_config_dir=USE_DEV_CONFIG_DIR):
    if use_dev_config_dir is not None:
        if use_dev_config_dir.lower() in {'false', '0'}:
            use_dev_config_dir = False
    else:
        use_dev_config_dir = DEV or not is_stable_version(__version__)

    return use_dev_config_dir


STDERR = sys.stderr


def get_debug_level():
    debug_env = os.environ.get('SPYDER_DEBUG', '')
    if not debug_env.isdigit():
        debug_env = bool(debug_env)
    return int(debug_env)


# ==============================================================================
# Configuration paths
# ==============================================================================
def get_conf_subfolder():
    if sys.platform.startswith('linux'):
        SUBFOLDER = 'bssrs'
    else:
        SUBFOLDER = '.bssrs'

    if use_dev_config_dir():
        SUBFOLDER = SUBFOLDER + '-dev'

    return SUBFOLDER


def get_module_path(modname):
    """Return module *modname* base path"""
    return osp.abspath(osp.dirname(sys.modules[modname].__file__))


def get_module_data_path(modname, relpath=None, attr_name='DATAPATH'):
    datapath = getattr(sys.modules[modname], attr_name, '')
    if datapath:
        return datapath
    else:
        datapath = get_module_path(modname)
        parentdir = osp.join(datapath, osp.pardir)
        if osp.isfile(parentdir):
            # Parent directory is not a directory but the 'library.zip' file:
            # this is either a py2exe or a cx_Freeze distribution
            datapath = osp.abspath(osp.join(osp.join(parentdir, osp.pardir),
                                            modname))
        if relpath is not None:
            datapath = osp.abspath(osp.join(datapath, relpath))
        return datapath


def get_module_source_path(modname, basename=None):
    srcpath = get_module_path(modname)
    parentdir = osp.join(srcpath, osp.pardir)
    if osp.isfile(parentdir):
        # Parent directory is not a directory but the 'library.zip' file:
        # this is either a py2exe or a cx_Freeze distribution
        srcpath = osp.abspath(osp.join(osp.join(parentdir, osp.pardir),
                                       modname))
    if basename is not None:
        srcpath = osp.abspath(osp.join(srcpath, basename))
    return srcpath


def is_py2exe_or_cx_Freeze():
    """Return True if this is a py2exe/cx_Freeze distribution of Spyder"""
    return osp.isfile(osp.join(get_module_path('bssrs'), osp.pardir))


# ==============================================================================
# Image path list
# ==============================================================================
IMG_PATH = []


def add_image_path(path):
    if not osp.isdir(path):
        return
    global IMG_PATH
    IMG_PATH.append(path)
    for dirpath, dirnames, _filenames in os.walk(path):
        for dirname in dirnames:
            IMG_PATH.append(osp.join(dirpath, dirname))


add_image_path(get_module_data_path('bssrs', relpath='images'))


def get_image_path(name, default="not_found.png"):
    """Return image absolute path"""
    for img_path in IMG_PATH:
        full_path = osp.join(img_path, name)
        if osp.isfile(full_path):
            return osp.abspath(full_path)
    if default is not None:
        img_path = osp.join(get_module_path('bssrs'), 'images')
        return osp.abspath(osp.join(img_path, default))
