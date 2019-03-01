class Templates:
    SETUP_PY = """from setuptools import setup


setup()"""
    SETUP_CFG = """[metadata]
name = %PACKAGE_NAME
version = 0.0.0
author = 
author_email = mcgela@mcgela.work
description = 
long_description = file:README.md
url = https://github.com/mcgela/
license = MIT
classifier =
    Development Status :: 1 - Planning
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
[options]
zip_safe = False
packages = find:"""
    README_MD = """# %PACKAGE_NAME
Made for me."""