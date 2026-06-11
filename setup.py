# This script sets up the environment for the app
# This script does the following things:-
#   * Sets up the Python virtual environment
#   * Installs needed module
#   * Downloads ADB if not found
#   * Makes backup.txt if not found
#   * Makes the destination directory for storing said backups

def createVE():
    import subprocess
    subprocess.run("python3 -m venv env")

def installModule():
    import subprocess, platform
    from pathlib import Path
    host = platform.system()
    install_path = Path("env")
    if host == "Windows":
        install_path = install_path / "Scripts" / "python3.exe"
    elif host in ["Darwin","Linux"]:
        install_path = install_path / "bin" / "python3"
    else:
        print("OS Unsupported")
        exit()
    subprocess.run(f"{install_path} -m pip install requests")

def createBackupList():
    print("Backup List Generator")
    with open("backup.txt","w") as f:
        while True:
            path = input("Enter the path you want to back up: ")
            if not path.startswith("/"):
                path = "/storage/emulated/0/" + path
            f.write(path)
            print("Path added successfully, any more paths to add?")
            choice = input("Enter yes or no: ")
            if choice.lower() not in "yes":
                break

def createDestination():
    import subprocess
    subprocess.run("mkdir Files")

if __name__ == "__main__":
    from pathlib import Path
    if not Path("env").is_dir():
        createVE()
        installModule()
    if not Path("backup.txt").exists():
        createBackupList()
    if not Path("Files").is_dir():
        createDestination()
