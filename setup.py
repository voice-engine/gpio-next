#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()


requirements = [
]

setup_requirements = [
    'wheel'
]

test_requirements = [
    'pytest'
]

setup(
    name='gpio-next',
    version='0.0.3',
    description="libgpiod python ctypes binding",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Yihui Xiong",
    author_email='yihui.xiong@hotmail.com',
    url='https://github.com/voice-engine/gpio-next',
    packages=find_packages(include=['gpio_next']),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
        ],
    },
    license='LGPLV2',
    zip_safe=False,
    keywords='gpio',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
