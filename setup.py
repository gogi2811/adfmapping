from setuptools import setup

setup(
    name='adfmapping',
    version='0.1.0',
    author='Gaurav Lotekar',
    py_modules=['adfmapping'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'adfmapping = adfmapping:get_dynamic_mapping',
        ],
    },
)