#!/usr/bin/python

"""
This installer script is compatible with python 3.5 only
"""
import sys
import os
from subprocess import call
import traceback

PIP_DOWNLOADLINK = r'https://bootstrap.pypa.io/get-pip.py'
PIP_FILENAME = "get-pip.py"
MAJOR_VER, MINOR_VER = sys.version_info[0:2]

def python_pip():

    if MAJOR_VER < 3:
        print("Python version atleast 3.5 is required \n Exiting...")
        sys.exit(1)
    elif MAJOR_VER > 3 and MINOR_VER < 5:
        print("Python version atleast 3.5 is required \n Exiting...")
        sys.exit(1)

    try:
        import pip
    except ImportError:
        print("Could not find pip on the system; Downloading....")
        try:
            if "darwin" == sys.platform:
                call(["easy_install", "pip"])
                return   
            else:
                from urllib.request import urlopen
                response = urlopen(PIP_DOWNLOADLINK)
                pathm = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
                get_pip = os.path.join(pathm, PIP_FILENAME)
                with open(pathm + os.sep + PIP_FILENAME, 'wb') as output:
                    output.write(response.read())
                print(get_pip)
                call(['python{}.{}'.format(MAJOR_VER, MINOR_VER), get_pip])
                return
        except:
            print("Error!!! PIP installation failed.")
            tb = traceback.format_exc()
            print(tb)
            sys.exit(1)


def install(package):
    pip.main(['install', package])

def pkg_check(imp_dict):
    for import_name in imp_dict.values():
        try:
            # print "import %s" %import_name
            __import__(import_name)
        except ImportError as e:
            print("Could not find %s on the system; Installing...." % import_name)
            # print e.message
            install(imp_dict[import_name])

if __name__ == '__main__':
    python_pip()
    from pip import _internal as pip
    package_dict = {
                       "csv": "csv",
                       "xlrd" : "xlrd"
                    }
    pkg_check(package_dict)

