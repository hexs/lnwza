import json
import os
from pprint import pprint
import sys
import lnwza
from lnwza._install_.install import install_package, upgrade_pip
from lnwza._proxy_ import proxy

if __name__ == '__main__':
    # r get
    if len(sys.argv) > 1:
        if sys.argv[1] == 'proxy':
            if len(sys.argv) == 3 and sys.argv[2] == 'get':
                proxy.get()

    # r set proxy_host 150.61.8.70
    if len(sys.argv) == 4 and sys.argv[1] == 'set':
        proxy.set(sys.argv[2], sys.argv[3])

    # r install x
    if len(sys.argv) == 3 and sys.argv[1] == 'install':
        print(sys.argv[1:])
        package_name = sys.argv[2]
        upgrade_pip()
        install_package(package_name)
