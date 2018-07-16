import conf
import json
import os
import platform
import sys
import yaml

# version
version = platform.python_version()
print("Python version: ", version)

# name(alias)
name_all = os.popen("pyenv versions --bare").read().strip().split("\n")
name_noal = (os.popen("pyenv versions --bare --skip-aliases")
             .read().strip().split("\n"))
namelist = []
for i in name_all:
    if i not in name_noal:
        namelist.append(i)
        print("List of aliases: ", namelist)

# virtual environment
if os.environ["VIRTUAL_ENV"]:
    venv = os.environ["VIRTUAL_ENV"]
    print("virtual environment: ", venv)
else:
    print("There is no virtual environment for current python version")
    exit(1)

# python executable location
execpath = sys.executable
print("Python executable location: ", execpath)

# pip location
pippath = os.popen("which pip").read().strip()
print("pip location path: ", pippath)

# PYTHONPATH
pypath = __file__
print("PYTHONPATH: ", pypath)

# installed packages
dict_pack = {}
list_pack = os.popen("pip freeze").read().strip().split("\n")
for i in list_pack:
    key = i.split("==")[0]
    value = i.split("==")[1]
    dict_pack[key] = value
print(dict_pack)


def get_json():
    result_json = {"version": version,
                   "name(alias)": namelist,
                   "virtual environment": venv,
                   "python executable location": execpath,
                   "pip location": pippath,
                   "PYTHONPATH": pypath,
                   "installed packages": dict_pack
                   }
    with open("output.json", "w") as dj:
        json.dump(result_json, dj, indent=4)


def get_yaml():
    result_yaml = {"version": version,
                   "name(alias)": namelist,
                   "virtual environment": venv,
                   "python executable location": execpath,
                   "pip location": pippath,
                   "PYTHONPATH": pypath,
                   "installed packages": dict_pack
                   }
    with open("output.yaml", "w") as ya:
        yaml.dump(result_yaml, ya, default_flow_style=False)


if conf.output == "json":
    get_json()
if conf.output == "yaml":
    get_yaml()
