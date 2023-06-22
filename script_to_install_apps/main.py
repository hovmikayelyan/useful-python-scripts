import os
import subprocess

def check_os():
    if os.name == 'posix':
        return 'linux'
    elif os.name == 'nt':
        return 'windows'
    elif os.name == 'darwin':
        return 'macos'
    else:
        return None

def read_apps():
    with open('apps.txt', 'r') as file:
        return file.read().splitlines()

def install_apps(apps, os_name):
    if os_name == 'linux':
        # Install apps on Linux using apt
        for app in apps:
            print(f"Installing {app} on Linux...")
            subprocess.run(['sudo', 'apt', 'install', '-y', app])
            
    elif os_name == 'windows':
        # Install Chocolatey package manager if not already installed
        if not is_chocolatey_installed():
            print("Chocolatey is not installed. Installing Chocolatey...")
            subprocess.run(['powershell.exe', '-Command', r"Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"])
        
        # Install apps on Windows using Chocolatey
        for app in apps:
            print(f"Installing {app} on Windows...")
            subprocess.run(['choco', 'install', '-y', app])
            
    elif os_name == 'macos':
        # Install Homebrew package manager if not already installed
        if not is_brew_installed():
            print("Homebrew is not installed. Installing Homebrew...")
            subprocess.run(['/bin/bash', '-c', "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])
        
        # Install apps on macOS using Homebrew
        for app in apps:
            print(f"Installing {app} on macOS...")
            subprocess.run(['brew', 'install', app])
            
    else:
        print("Unsupported operating system.")

def is_chocolatey_installed():
    try:
        subprocess.run(['choco', '--version'], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def is_brew_installed():
    try:
        subprocess.run(['brew', '--version'], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Check the operating system
os_name = check_os()
if os_name:
    print(f"Detected OS: {os_name}")
    # Read the list of apps from apps.txt
    apps = read_apps()
    print(f"Apps to install: {apps}")
    # Install the apps
    install_apps(apps, os_name)
else:
    print("Unable to detect the operating system.")
