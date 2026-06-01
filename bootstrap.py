import sys
import subprocess
import os

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    return process.poll()

def main():
    print("--- Bootstrapping MkDocs Documentation Environment ---")
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if not os.path.exists(req_path):
        print(f"Error: Could not find requirements.txt at {req_path}")
        sys.exit(1)

    print(f"\nInstalling dependencies from {req_path}...")
    install_code = run_command(f'"{sys.executable}" -m pip install -r "{req_path}"')
    
    if install_code == 0:
        print("\nInstallation successful")
    else:
        print("\nError: Installation failed. Please check the logs above.")
        sys.exit(install_code)

if __name__ == "__main__":
    main()