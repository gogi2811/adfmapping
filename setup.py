from setuptools import setup

setup(
    name='adfmapping',
    version='0.1.0',
    author='Gaurav Lotekar',
    author_email='gauravnlotekar@gmail.com',
    url='https://github.com/gogi2811/adfmapping',
    keywords='Azure ADF mapping ADF mapping JSON json',
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