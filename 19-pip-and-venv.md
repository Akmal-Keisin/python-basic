# Python PIP & Virtual Environments (`venv`)

## The "Why" (The Dependency Hell Problem)

In Node.js, when you run `npm install`, packages go into a local `node_modules` folder. In Python, by default, `pip` installs packages **globally** on your computer.

**The Problem:**
Imagine Project A needs `Django 3.0` and Project B needs `Django 5.0`. If you install them globally, one will overwrite the other, breaking your code.

**The Solution:**
**Virtual Environments (`venv`).** This is Python's way of creating a local `node_modules` or `vendor` folder specific to *one* project.

## Virtual Environments (`venv`)

`venv` is a module included in Python (standard library) to create lightweight "virtual" Python installations.

### How to Create one

Go to your project folder in your terminal and run:

```bash
# Windows / Mac / Linux
python -m venv .venv
```

  * `python -m venv`: Tells Python to run the `venv` module.
  * `.venv`: The name of the folder to create. (Standard convention is `.venv` or `venv`).

### How to Activate it

This is the most critical step. If you don't activate it, you are still using the global Python.

  * **Windows (Command Prompt):**
    ```cmd
    .venv\Scripts\activate
    ```
  * **Windows (PowerShell):**
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
  * **Mac / Linux:**
    ```bash
    source .venv/bin/activate
    ```

**How do you know it worked?**
Your terminal prompt will change to show the environment name:
`(venv) user@computer:~/project$`

### How to Deactivate

When you are done working, simply type:

```bash
deactivate
```

-----

## Python PIP (The Package Installer)

**PIP** is the package installer for Python (equivalent to `npm` or `composer`). It connects to **PyPI** (Python Package Index), which is the repository for open-source software (like Packagist or npmjs).

### Installing Packages

Once your `venv` is active:

```bash
# Install the latest version
pip install requests

# Install a specific version (HIGHLY RECOMMENDED)
pip install requests==2.31.0

# Install logic:
# >= : Greater than or equal to
pip install "requests>=2.0"
```

### Managing Packages

```bash
# List installed packages
pip list

# Show details about a specific package (location, dependencies)
pip show requests

# Uninstall a package
pip uninstall requests
```

-----

## The Relation (Workflow & Reproducibility)

In Laravel, you have `composer.json` and `composer.lock`. In Python, we use a file called `requirements.txt`.

### The Workflow:

1.  **Create/Activate Venv:** You build the isolated sandbox.
2.  **Pip Install:** You install libraries into that sandbox.
3.  **Freeze:** You save the list of libraries so others can run your code.

### Generating `requirements.txt` (Freezing)

After installing your packages, run this to save the list:

```bash
pip freeze > requirements.txt
```

*This creates a file listing every installed package and its exact version.*

### Installing from `requirements.txt`

When you clone a repo or move to a server, you run:

```bash
pip install -r requirements.txt
```

*This is equivalent to `npm install` (reading package.json).*

-----

## Advanced PIP Features

### Upgrade Packages

```bash
pip install --upgrade requests
```

### Check for Conflicts

Sometimes dependencies clash (Lib A wants NumPy 1.0, Lib B wants NumPy 2.0).

```bash
pip check
```

### Caching

PIP caches downloads locally to speed up future installs. If things get weird, you can clear it:

```bash
pip cache purge
```

### Editable Installs (`-e`)

*Used when developing a library.*
If you are writing a library and want to test it in another project without constantly reinstalling it:

```bash
pip install -e path/to/your/library
```

Any change you make to the source code is immediately reflected in the environment.

-----

## Best Practices (The "Professional" Way)

### ALWAYS use a Virtual Environment

Never install packages globally (`pip install x`) unless it is a system-wide tool (like `black` formatter or `aws-cli`). For projects, always use `venv`.

### The `.gitignore` Rule

**Never** commit your `.venv` folder to Git. It is huge and specific to your machine (OS dependent).
**Add this to `.gitignore`:**

```text
.venv/
venv/
__pycache__/
*.pyc
```

### Pin Your Versions

Don't just use `pip install pandas`. Use `pip install pandas==2.0.3`. This prevents your application from breaking if a new "breaking change" update is released tomorrow.

### Upgrade Pip Itself

Pip is just a Python package. It's good practice to keep it updated.

```bash
python -m pip install --upgrade pip
```

### Requirements Structure (For Large Projects)

For complex apps, you might split your requirements:

  * `requirements.txt` (Production base)
  * `requirements-dev.txt` (Testing tools, linters)

**Content of `requirements-dev.txt`:**

```text
-r requirements.txt
pytest
black
flake8
```

-----

### Comparison with your Stack

| Feature           | Python                      | Node.js (Vue)                 | PHP (Laravel)          |
| :---------------- | :-------------------------- | :---------------------------- | :--------------------- |
| **Repo/Registry** | PyPI                        | npm registry                  | Packagist              |
| **Installer**     | pip                         | npm / yarn                    | composer               |
| **Manifest File** | requirements.txt            | package.json                  | composer.json          |
| **Isolation**     | venv                        | node\_modules (local default) | vendor (local default) |
| **Lock File**     | requirements.txt (manual)\* | package-lock.json             | composer.lock          |

*\*Note: Modern Python tools like `Poetry` or `Pipenv` introduce real lock files, but `pip` + `venv` is the industry standard foundation.*