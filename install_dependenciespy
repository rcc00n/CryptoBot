import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of packages to install
packages = ['bybit', 'pandas', 'requests']  # Add other necessary packages here

for package in packages:
    install(package)
