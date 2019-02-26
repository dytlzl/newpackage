import sys
import os
from templates import templates


class gen_new_package():
    def __init__(self, package_name):
        self.package_name = package_name
        self.main()


    def main(self):
        self.create_dir(self.package_name)
        with open(self.package_name+'/setup.py', mode='w') as file:
            file.write(templates)
        child_path = self.package_name+'/'+self.package_name
        self.create_dir(child_path)
        with open(child_path+'/__init__.py', mode='w') as file:
            pass
        with open(child_path+'/__main__.py', mode='w') as file:
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
        gen_new_package(args[1])
    except DirectoryAlreadyExistsError:
        print('Directory Alredy Exists.')


if __name__ == "__main__":
    main()