import os
import subprocess
import sys

# Check if the virtual environment exists in the current directory and create it if it does not
#venv_name = os.path.basename(os.getcwd())  # Use the current directory name for the venv
#venv_path = os.path.join(os.getcwd(), venv_name)
#if not os.path.exists(venv_path):
#    subprocess.check_call([sys.executable, "-m", "venv", venv_name])
#    print(f"Created virtual environment {venv_name} in {venv_path}.")
#    print(f"Please activate the virtual environment with `{os.path.join(venv_path, 'bin', 'activate')}` on Unix or `{os.path.join(venv_path, 'Scripts', 'activate')}` on Windows and re-run this script.")
#    sys.exit(0)

# Dictionary of packages to install, mapping module names to their respective package names
packages = {"bs4": "beautifulsoup4"}
for module_name, package_name in packages.items():
    try:
        __import__(module_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

