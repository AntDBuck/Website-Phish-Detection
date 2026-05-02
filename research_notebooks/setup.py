import os
import sys
import subprocess

# Automatic setup of python virtual enviroment and the installing of dependencies.

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_PATH = os.path.join(ROOT_DIR, '.venv')
REQUIREMENTS_PATH = os.path.join(ROOT_DIR, 'requirements.txt')

def check_create_venv():
    print('Checking if virtual environment exists...')

    if os.path.isdir(VENV_PATH):
        print('Virtual environment exists. Skipping creation of new .venv...')
    else:
        print('No .venv found. Creating...')
        subprocess.check_call([sys.executable, '-m', 'venv', VENV_PATH])

def get_venv_python():
    if os.name == 'nt':
        return os.path.join(VENV_PATH, 'Scripts', 'python.exe')
    else:
        return os.path.join(VENV_PATH, 'bin', 'python')

def install_requirements(venv_python):
    if not os.path.isfile(REQUIREMENTS_PATH):
        print('Error: requirements.txt not found. Exiting...')
        sys.exit(2)

    print('Installing dependencies...')
    subprocess.check_call([venv_python, '-m', 'pip', 'install', '-r', REQUIREMENTS_PATH])

def main():
    check_create_venv()
    venv_python = get_venv_python()
    install_requirements(venv_python)
    print('\n--- Setup completed! ---')
    print('Activate virtual environment:\n')
    print(r'Windows > .venv\Scripts\activate')
    print(r'MacOS/Linux > source .venv\bin\activate')
    print('Run jupyter lab with > jupyter lab')

if __name__ == '__main__':
    main()