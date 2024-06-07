import os
import subprocess
import sys


def create_install_bat(venv_path, package_name_list, proxy_http=None):
    package_name = ' '.join(package_name_list)
    activate_bat_file = os.path.join(venv_path, r'Scripts\activate.bat')
    txt = f'@echo off\n'
    txt += f'call "{activate_bat_file}"\n'
    if proxy_http:
        txt += f'python -m pip install --proxy {proxy_http} {package_name}\n'
    else:
        txt += f'python -m pip install {package_name}\n'
    with open('run.bat', 'w') as f:
        f.write(txt)


def create_other_bat(venv_path, comm):
    command = ' '.join(comm)
    activate_bat_file = os.path.join(venv_path, r'Scripts\activate.bat')
    txt = f'@echo off\n'
    txt += f'call "{activate_bat_file}"\n'
    txt += f'python -m pip {command}\n'
    with open('run.bat', 'w') as f:
        f.write(txt)


def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        print(f"error delete file {file_path}")


def install_package(venv_path, package_name_list):
    res = subprocess.run("git config --global https.proxy", capture_output=True)
    proxy_http = res.stdout.decode().strip()

    create_install_bat(venv_path, package_name_list, proxy_http)

    subprocess.run("run.bat", shell=True)

    delete_file('run.bat')


def other(venv_path, comm):
    create_other_bat(venv_path, comm)
    subprocess.run("run.bat", shell=True)
    delete_file('run.bat')


def pipp():
    if len(sys.argv) >= 2 and sys.argv[1] == 'install' and len(sys.argv) >= 3:
        package_name_list = sys.argv[2:]
        dir_ = os.path.dirname(__file__)
        while True:
            if 'Scripts' in os.listdir(dir_):
                break
            else:
                dir_ = os.path.split(dir_)[0]
        install_package(dir_, package_name_list)


    else:
        comm = sys.argv[1:]
        dir_ = os.path.dirname(__file__)
        while True:
            if 'Scripts' in os.listdir(dir_):
                break
            else:
                dir_ = os.path.split(dir_)[0]
        other(dir_, comm)
        if len(sys.argv) == 1:
            print(
                'pip auto proxy form\tgit config --global https.proxy\n'
                'upgrade pip can use\tpip install --upgrade pip'
            )
