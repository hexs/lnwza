import os
import subprocess
import lnwza
from ..constant import *
from lnwza._proxy_.proxy import config_proxy, proxy_link


def install_package(package_name):
    print(f'installing... {package_name}')
    try:
        print(BLUE, end='')
        if config_proxy.get('used_proxy'):
            subprocess.run(f"python -m pip install --proxy {proxy_link} {package_name}", check=True)
        else:
            subprocess.run(f"python -m pip install {package_name}", check=True)
        print(f"{package_name} installed successfully.")
        print(BLUE, end='')
    except Exception as e:
        prin(RED)
        print(f"Failed to install {package_name}. Error: {str(e)}")
        print(BLUE, end='')


def upgrade_pip():
    try:
        if config_proxy.get('used_proxy'):
            subprocess.run(f"python -m pip install --proxy {proxy_link} --upgrade pip", check=True)
        else:
            subprocess.run("python -m pip install --upgrade pip", check=True)
        print(f"{BLUE}upgrade pip installed successfully.{ENDC}")
    except Exception as e:
        print(f"{RED}Failed to upgrade pip. Error: {str(e)}{ENDC}")
