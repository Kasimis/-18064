import os
import winreg
import pythoncom
from win32com.shell import shell

def get_installed_programs():
    """Retrieve a list of installed programs from the Windows registry."""
    installed_programs = set()
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
    ]

    for registry_path in registry_paths:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            installed_programs.add(display_name.lower())
                        except FileNotFoundError:
                            continue
        except FileNotFoundError:
            continue

    return installed_programs

def get_target_from_shortcut(lnk_path):
    """Extract the target path from a shortcut file."""
    try:
        shell_link = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink
        )
        persist_file = shell_link.QueryInterface(pythoncom.IID_IPersistFile)
        persist_file.Load(lnk_path)
        target, _ = shell_link.GetPath(shell.SLGP_SHORTPATH)
        return target
    except Exception as e:
        print(f"Error reading shortcut {lnk_path}: {e}")
        return None

def remove_uninstalled_shortcuts(desktop_path, installed_programs):
    """Remove shortcuts on the desktop pointing to uninstalled programs."""
    for item in os.listdir(desktop_path):
        if item.endswith(".lnk"):
            shortcut_path = os.path.join(desktop_path, item)
            print(f"Processing shortcut: {shortcut_path}")
            target_path = get_target_from_shortcut(shortcut_path)

            if target_path:
                target_lower = target_path.lower()
                # Check if the shortcut points to an uninstalled program
                if not any(program in target_lower for program in installed_programs):
                    try:
                        os.remove(shortcut_path)
                        print(f"Removed shortcut: {shortcut_path}")
                    except Exception as e:
                        print(f"Error removing {shortcut_path}: {e}")
            else:
                print(f"Could not retrieve target for {shortcut_path}")

def main():
    desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
    installed_programs = get_installed_programs()

    print("Installed Programs Retrieved.")
    print(f"Total installed programs: {len(installed_programs)}")
    
    print("\nScanning desktop for shortcuts...")
    remove_uninstalled_shortcuts(desktop_path, installed_programs)

if __name__ == "__main__":
    main()
