from setuptools import setup

setup(
    name='vocalhost-python',
    version='1.0.0',
    py_modules=['vocalhost'],
    install_requires=[
        'websockets',
        'certifi'
    ]
)