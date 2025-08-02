import os
import platform
import subprocess


SYSTEM = platform.system()
PYTHON_EXEC = "python" if SYSTEM == "Windows" else "python3"
MANAGE_PY = f"{PYTHON_EXEC} manage.py"
VENV_DIR = ".venv"

def run_command(command):
    if SYSTEM == 'Linux':
        command = f"/bin/bash -c '{command}'"

    process = subprocess.Popen(command, shell=True)
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

    print("Aplying Django migrations...")
    run_command(f"{activate} && {MANAGE_PY} migrate")

    create_superuser = input("Create superuser? (y/n): ").strip().lower()
    if create_superuser == 'y':
        run_command(f"{activate} && {MANAGE_PY} createsuperuser")

    print("Starting Django server in http://localhost:8000 ...")
    run_command(f"{activate} && {MANAGE_PY} runserver")

if __name__ == "__main__":
    main()
