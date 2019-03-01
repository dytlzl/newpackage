import sys
import os
from .constants import Templates


class GenNewPackage():
    def __init__(self, package_name):
        self.package_name = package_name
        self.main()


    def main(self):
        self.create_dir(self.package_name)
        with open(self.package_name+'/setup.py', mode='w') as file:
            file.write(Templates.SETUP_PY)
        with open(self.package_name+'/README.md', mode='w') as file:
            file.write(Templates.README_MD.replace('%PACKAGE_NAME', self.package_name))
        with open(self.package_name+'/setup.cfg', mode='w') as file:
            file.write(Templates.SETUP_CFG.replace('%PACKAGE_NAME', self.package_name))
        child_path = self.package_name+'/'+self.package_name
        self.create_dir(child_path)
        with open(child_path+'/__init__.py', mode='w') as file:
            pass
    

    @staticmethod
    def create_dir(package_name):
        if os.path.exists(package_name):
            raise DirectoryAlreadyExistsError
        else:
            os.mkdir(package_name)


class DirectoryAlreadyExistsError(Exception):
    pass


def main():
    args = sys.argv
    try:
        GenNewPackage(args[1])
    except DirectoryAlreadyExistsError:
        print('Directory Already Exists.')


if __name__ == "__main__":
    main()