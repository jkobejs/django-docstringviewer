import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-docstringviewer',
    version='0.1',
    packages=['docstringviewer', ],
    include_package_data=True,
    license='New BSD License',  
    description='A Django app to view docstring of modules and its object inside project.',
    long_description=README,
    url='http://www.example.com/',
    author='Josip Grgurica & Ivan Zderic',
    author_email='josip.grgurica@gmail.comm',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Djangp'
    ],
    install_requires=['setuptools', 'django>=1.4',],
)
