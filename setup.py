from setuptools import setup

APP = ['Health.py']
DATA_FILES = [('./assets', ['./assets/icon.png'])]
OPTIONS = {
    'packages': ['rumps', 'schedule'],
    'plist': {
        'LSUIElement': 1, 
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
