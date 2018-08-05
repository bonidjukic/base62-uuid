import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='base62-uuid',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django App which provides Base62UUIDMixin',
    long_description=README,
    url='git@github.com/bonidjukic/base62-uuid.git',
    author='Boni Đukić',
    author_email='boni@djukic.com.hr',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)
