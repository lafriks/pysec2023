# PySec 2023

## Python installation

```sh
sudo apt install python2 python3
```

```console
❯ python2 --version
Python 2.7.18

❯ python3 --version
Python 3.10.12
```

## virtualenv

### Create

```sh
python3 -m venv .venv
```

### Usage

```sh
source .venv/bin/activate
```

```console
pysec23 on  main [!] 
❯ source .venv/bin/activate

pysec23 on  main [!] via 🐍 v3.10.12 (.venv) 
❯ python --version
Python 3.10.12
```

### Install dependencies

```sh
pip3 install -r requirements.txt
```
