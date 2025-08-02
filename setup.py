import os
import secrets
import platform
import subprocess


SYSTEM = platform.system()
PYTHON_EXEC = "python" if SYSTEM == "Windows" else "python3"
MANAGE_PY = f"{PYTHON_EXEC} manage.py"
VENV_DIR = ".venv"
ENV_PATH = os.path.join('app', '.env')

def run_command(command, background=False):
    if SYSTEM == 'Linux':
        command = f"/bin/bash -c '{command}'"

    process = subprocess.Popen(command, shell=True)

    if not background:
        process.communicate()

def main():
    print(f"System: {SYSTEM}")

    if not os.path.exists(VENV_DIR):
        print("Creating '.venv'...")
        run_command(f"{PYTHON_EXEC} -m venv {VENV_DIR}")

    if SYSTEM == "Windows":
        activate = os.path.join(VENV_DIR, "Scripts", "activate")
    else:
        activate = f"source {VENV_DIR}/bin/activate"

    print("Installing dependencies...")
    run_command(f"{activate} && pip install -r requirements.txt")

    if not os.path.exists(ENV_PATH):
        print("Creating '.env'...")
        with open(ENV_PATH, 'w', encoding='utf-8') as file:
            file.write(f'DJANGO_DEBUG=0\nALLOWED_HOSTS=*\nDJANGO_SECRET_KEY={secrets.token_hex(64)}')
        print(f"'{ENV_PATH}' created.")

    print("Aplying Django migrations...")
    run_command(f"{activate} && {MANAGE_PY} migrate")

    create_superuser = input("Create superuser? (y/n): ").strip().lower()
    if create_superuser == 'y':
        run_command(f"{activate} && {MANAGE_PY} createsuperuser")

    print("Starting Django server in http://localhost:8000 ...")
    run_command(f"{activate} && {MANAGE_PY} runserver")


if __name__ == "__main__":
    main()
