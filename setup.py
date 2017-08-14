import os
from setuptools import setup, find_packages

import comment


with open('README.md') as f:
    README = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-comment',
    version=comment.version,
    packages=find_packages(exclude=('test*',)),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to add comment and related operations to your models.',
    long_description=README,
    url='https://github.com/shanbay/django-comment',
    author='Will Skywalker',
    author_email='me@willskywalker.com',
    install_requires=['django', 'django-vote'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
