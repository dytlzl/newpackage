import sys
import os
from .constants import Templates


class GenNewPackage:
    def __init__(self, package_name):
        self.package_name = package_name
        self.main()

    def main(self):
        create_dir(self.package_name)
        create_file(self.package_name+'/setup.py', Templates.SETUP_PY)
        create_file(self.package_name+'/README.md', Templates.README_MD.replace('%PACKAGE_NAME', self.package_name))
        create_file(self.package_name+'/setup.cfg', Templates.SETUP_CFG.replace('%PACKAGE_NAME', self.package_name))
        child_path = self.package_name+'/'+self.package_name
        create_dir(child_path)
        with open(child_path+'/__init__.py', mode='w'):
            pass


def create_dir(package_name):
    if os.path.exists(package_name):
        print('Directory Already Exists.')
        sys.exit()
    else:
        os.mkdir(package_name)


def create_file(filename, string):
    with open(filename, mode='w') as file:
        file.write(string)


def main():
    args = sys.argv
    GenNewPackage(args[1])
