import platform
import shutil
import sys


def check_system():
    _python_command = "python" if platform.system() == "Windows" else "python3"
    if int(platform.python_version_tuple()[1]) < 10:
        print("Please use Python 3.10+")
        sys.exit()

    if not shutil.which("poetry"):
        print("Poetry not found, please install poetry by running this commands:")
        print(f"curl -sSL https://install.python-poetry.org | {_python_command} -")
        print(
            r"set PATH=%PATH%;%USERPROFILE%\AppData\Roaming\pypoetry\venv\Scripts"
            if _python_command == "python"
            else 'export PATH="$HOME/.local/bin:$PATH'
        )


def run_game():
    # pylint: disable=import-outside-toplevel
    from game import main

    main()


if __name__ == "__main__":
    check_system()
