import requests
from cx_Freeze import setup, Executable
import sys, os
from idna import idnadata
from multiprocessing import Queue
import os

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

sys.argv.append("build")
filename="Synopsize.py"
icon= "cap.ico"

base = None

options={
        "build_exe": {
            "packages": ["idna"],
            },
        },

if sys.platform=="win64":
    base="Win64GUI"

exe = Executable(script='Synopsize.py', base = base, icon='cap.ico')

additional_mods = ['scipy.spatial.ckdtree', 'html.parser', 'numpy.core._methods', 'numpy.lib.format']
additional_packages = ['HTMLParser', 'tkinter', 'scipy.sparse.csgraph._validation', 'asyncio', 'asyncio.compat', 'appdirs', 'csv', 'pkg_resources._vendor']

setup(
    name = "Synopsize",
    version = "1.0",
    description = 'Synopsize',
    author = 'Wakili.AI',
    author_email = 'mwago.gatahi@gmail.com',
    options = {
        'build_exe': {
            'includes': additional_mods,
            'packages': additional_packages,
            'include_files':[
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                ],
            
        }},
    executables=[exe])


