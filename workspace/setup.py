from setuptools import setup

setup(
    name='workspace',
    version='0.1.1',
    py_modules=['workspace'],
    install_requires=[
        'cLick',
    ],
    entry_points={
        "console_scripts": [
            'workspace = workspace:initworkspace',
        ],
    },
)