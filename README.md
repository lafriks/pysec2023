# PySec 2023

## Python installation

Use .devcontainers or install on host using following commands:

```sh
sudo apt install python3.9 python3.11
```

Test both python versions are available:

```console
vscode ➜ /workspaces/pysec23 (main) $ python3.9 --version
Python 3.9.2
vscode ➜ /workspaces/pysec23 (main) $ python3.11 --version
Python 3.11.4
```

## virtualenv

### Create

```sh
python3.9 -m venv .venv3.9
python3.11 -m venv .venv
```

### Usage

```sh
source .venv/bin/activate
```

```console
vscode ➜ /workspaces/pysec23 (main) $ source .venv3.9/bin/activate
(.venv3.9) vscode ➜ /workspaces/pysec23 (main) $ python --version
Python 3.9.2
(.venv3.9) vscode ➜ /workspaces/pysec23 (main) $ deactivate

vscode ➜ /workspaces/pysec23 (main) $ source .venv/bin/activate
(.venv) vscode ➜ /workspaces/pysec23 (main) $ python --version
Python 3.11.4
```

### Install dependencies

```sh
pip3 install -r requirements.txt
```
