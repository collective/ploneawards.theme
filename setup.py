# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '0.2.dev0'
long_description = (
    open('README.rst').read() + '\n' +
#    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='ploneawards.theme',
      version=version,
      description="Cursuscentrale Theme",
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Software Development :: User Interfaces",
      ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/ploneawards.theme',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneawards'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.registry',
          'plone.app.theming',
          'plone.app.themingplugins',
          'setuptools',
          'z3c.jbot',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.testing',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
