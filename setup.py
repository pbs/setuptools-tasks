#!/usr/bin/env python

from setuptools import setup, find_packages


LONG_DESCRIPTION = open('README.rst').read()


setup(
    name='setuptools-tasks',
    version='0.1.0',
    description='Augments setuptools lifecycle.',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='setuptools sass',
    author='PBS Bento Web Services Team',
    author_email='TPG-PBS-Bento@3pillarglobal.com',
    maintainer_email='TPG-PBS-Bento@3pillarglobal.com',
    url='https://github.com/pbs/setuptools-tasks',
    packages=find_packages(),
    include_package_data=True,
    platforms=['any'],
    install_requires=['setuptools'],
    entry_points={
        'distutils.commands': [
            'sdist = setuptools_tasks.sdist:sdist',
            'build_static_files = setuptools_tasks.statics_building:BuildStaticFiles',
        ]
    }
)
