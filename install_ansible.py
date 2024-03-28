import platform
import subprocess

def check_ansible_installed():
    try:
        subprocess.run(["ansible", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_ansible():
    os_name = platform.system()
    if os_name == "Linux":
        distro = platform.dist()[0].lower()
        if distro in ["centos", "redhat", "rocky", "oracle", "fedora"]:
            install_ansible_rhel()
        elif distro in ["ubuntu", "debian"]:
            install_ansible_debian()
        elif distro in ["suse"]:
            install_ansible_suse()
        else:
            print("Unsupported Linux distribution:", distro)
    elif os_name == "Darwin":
        install_ansible_mac()
    else:
        print("Unsupported operating system:", os_name)

def install_ansible_rhel():
    if check_ansible_installed():
        print("Ansible is already installed on RHEL-based system.")
    else:
        try:
            subprocess.run(["sudo", "yum", "install", "ansible", "-y"], check=True)
            print("Ansible installed successfully on RHEL-based system.")
        except subprocess.CalledProcessError as e:
            print("Error installing Ansible on RHEL-based system:", e)

def install_ansible_debian():
    if check_ansible_installed():
        print("Ansible is already installed on Debian-based system.")
    else:
        try:
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "ansible", "-y"], check=True)
            print("Ansible installed successfully on Debian-based system.")
        except subprocess.CalledProcessError as e:
            print("Error installing Ansible on Debian-based system:", e)

def install_ansible_suse():
    if check_ansible_installed():
        print("Ansible is already installed on SUSE-based system.")
    else:
        try:
            subprocess.run(["sudo", "zypper", "install", "ansible", "-y"], check=True)
            print("Ansible installed successfully on SUSE-based system.")
        except subprocess.CalledProcessError as e:
            print("Error installing Ansible on SUSE-based system:", e)

def install_ansible_mac():
    if check_ansible_installed():
        print("Ansible is already installed on macOS.")
    else:
        try:
            subprocess.run(["brew", "install", "ansible"], check=True)
            print("Ansible installed successfully on macOS.")
        except subprocess.CalledProcessError as e:
            print("Error installing Ansible on macOS:", e)

if __name__ == "__main__":
    install_ansible()
