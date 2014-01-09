"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2exe
"""

import os
import py2exe
from distutils.core import setup

from circuitscape import __version__, __author__, __email__

INCLUDES =[]
PACKAGES = ['PythonCard', 'wx', 'wxversion', 'numpy', 'scipy', 'pyamg', "scipy.io.matlab.streams"]

DATA_FILES = ['circuitscape/cs_logo.jpg', 'circuitscape/gui_rsrc.py', 'cs_logo.ico'] 
 
OPTIONS = {'includes': PACKAGES}


# Compile cs_run.py first to ensure that dependencies needed for cs_gui also included.
setup(
    console=['bin/csrun.py'],
    data_files=DATA_FILES,
    options={'py2exe': OPTIONS},
    version=__version__,
    author= __author__,
    author_email=__email__
)
setup(
    console = [
        {
            "script": "bin/csgui.py",
            "icon_resources": [(1, "cs_logo.ico")]
        }
    ],
    data_files=DATA_FILES,
    options={'py2exe': OPTIONS},
    version=__version__,
    author= __author__,
    author_email=__email__
)

import os, shutil
# Copy subdirectories
if os.path.exists('dist/circuitscape'): 
    shutil.rmtree('dist/circuitscape')
if os.path.exists('dist/examples'): 
    shutil.rmtree('dist/examples')
shutil.copytree('circuitscape/verify', 'dist/circuitscape/verify')
shutil.copytree('examples', 'dist/examples')

# Rename command line executable for backward compatibility
if os.path.exists('dist/cs_run.exe'):
    os.remove('dist/cs_run.exe')
os.rename('dist/csrun.exe','dist/cs_run.exe')

# Note: if having pythoncard problems see  http://www.py2exe.org/index.cgi/PythonCardSetup 