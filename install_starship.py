import platform
import os
import subprocess
import shutil

SUPPORTED_PLATFORMS = ["macOS", "Linux"]
SUPPORTED_SHELLS = ["bash", "zsh"]

def check_platform():
    os_name = platform.system()
    if os_name == "Darwin":
        print("You are on macOS.")
        return "macOS"
    elif os_name == "Linux":
        print("You are on Linux.")
        return "Linux"
    else:
        print("Your platform is not supported.")
        return None

def check_shell():
    shell_type = os.environ.get("SHELL")
    if shell_type:
        if "zsh" in shell_type:
            print("Your shell is Zsh.")
            return "zsh"
        elif "bash" in shell_type:
            print("Your shell is Bash.")
            return "bash"
        else:
            print("Your shell type is not recognized.")
            return None
    else:
        print("Unable to determine the shell type.")
        return None

def install_starship():
    platform_type = check_platform()
    if platform_type in SUPPORTED_PLATFORMS:
        subprocess.run(["curl", "-sS", "https://starship.rs/install.sh"], check=True)
    else:
        print("Starship installation is not supported on this platform.")

def add_starship_to_shell():
    shell_type = check_shell()
    if shell_type in SUPPORTED_SHELLS:
        if shell_type == "bash":
            if not is_configured("~/.bashrc", 'eval "$(starship init bash)"'):
                subprocess.run(["eval", '"$(starship init bash)"'], shell=True, check=True)
                with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
                    bashrc.write('\n' + 'eval "$(starship init bash)"')
        elif shell_type == "zsh":
            if not is_configured("~/.zshrc", 'eval "$(starship init zsh)"'):
                subprocess.run(["eval", '"$(starship init zsh)"'], shell=True, check=True)
                with open(os.path.expanduser("~/.zshrc"), "a") as zshrc:
                    zshrc.write('\n' + 'eval "$(starship init zsh)"')
    else:
        print("Can't configure starship with the current shell:", shell_type)

def copy_starship_config():
    try:
        shutil.copy("starship_pastel_with_os.toml", os.path.expanduser("~/.config/starship.toml"))
        print("Starship configuration file copied successfully.")
    except FileNotFoundError:
        print("Error: Unable to find the starship_pastel_with_os.toml file.")

def is_configured(file_path, line):
    if not os.path.exists(os.path.expanduser(file_path)):
        return False
    with open(os.path.expanduser(file_path), "r") as file:
        lines = file.readlines()
        for l in lines:
            if line.strip() in l.strip():
                return True
    return False

def setup_starship():
    platform_type = check_platform()
    shell_type = check_shell()
    if platform_type in SUPPORTED_PLATFORMS and shell_type in SUPPORTED_SHELLS:
        install_starship()
        add_starship_to_shell()
        copy_starship_config()
    else:
        print("Your platform or shell is not supported.")

if __name__ == "__main__":
    setup_starship()
