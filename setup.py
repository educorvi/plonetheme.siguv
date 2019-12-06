# -*- coding: utf-8 -*-
"""Installer for the plonetheme.siguv package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='plonetheme.siguv',
    version='1.1.0.dev0',
    description="A Plone 5.2 Theme for the siguv cooperation. Based on collective/plonetheme.tokyo !",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Stefan Arnold',
    author_email='stefan.arnold@operun.de',
    url='https://pypi.python.org/pypi/plonetheme.siguv',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plonetheme'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.themefragments',
        'collective.themesitesetup',
        'plone.api>=1.8.4',
        'plone.app.themingplugins',
        'plonetheme.tokyo',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
            'plone.app.testing',
            'plone.testing>=5.0.0',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plonetheme.siguv.locales.update:update_locale
    """,
)
