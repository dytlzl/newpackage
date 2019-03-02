class Templates:
    SETUP_PY = """from setuptools import setup


setup()"""
    SETUP_CFG = """[metadata]
name = %PACKAGE_NAME
version = 0.0.0
author = 
author_email =
description = 
long_description = file:README.md
url = 
license = MIT
classifier =
    Development Status :: 1 - Planning
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.7
[options]
zip_safe = False
packages = find:
[options.entry_points]
console_scripts =
    newpackage = newpackage.app:main"""
    README_MD = """# %PACKAGE_NAME
FOR MY OWN USE."""
