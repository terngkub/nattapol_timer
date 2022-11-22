from setuptools import setup

setup(
    name = 'nattapol_timer',
    version='0.0.1',
    packages = ['timer'],
    entry_points = {
        "console_scripts": [
            'nattapol-timer = timer.__main__:main',
        ]
    },
    install_requires=['chime'],
)
