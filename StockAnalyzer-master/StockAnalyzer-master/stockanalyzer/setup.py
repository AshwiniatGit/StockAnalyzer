from setuptools import setup

APP = ['GUI.py']
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'stockIcon.icns'}
DATA_FILES = [('', ['assets'])]

setup(
    app=APP,
    data_files=DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires=["py2app"],
)
