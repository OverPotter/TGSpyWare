import os
from typing import TypeVar
from config import PROJECT_TEMP_DIR, BASE_DIR, MAIN_FILE_NAME, AUTORUN_NAME, RUN_FILENAME, BAT_FILENAME, PYTHON_VENV_PATH
from winreg import OpenKey, SetValueEx, DeleteValue, CloseKey, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ

# generic annotations
PyHKEY = TypeVar("PyHKEY")


class RegEdit:
    def __init__(self):
        self.autorun_path: str = os.path.join(PROJECT_TEMP_DIR, RUN_FILENAME)
        self.bat_file_path: str = os.path.join(PROJECT_TEMP_DIR, BAT_FILENAME)
        self.key_reg: PyHKEY = OpenKey(HKEY_CURRENT_USER,
                                       r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                                       0, KEY_ALL_ACCESS)

    def __create_temp_files(self):
        with open(self.bat_file_path, "w") as file:
            file.write(f"{os.path.join(BASE_DIR, PYTHON_VENV_PATH)} {os.path.join(BASE_DIR, MAIN_FILE_NAME)}")

        with open(self.autorun_path, "w") as file:
            file.write(f'Set WshShell = CreateObject("WScript.Shell")\n'
                       f'WshShell.Run chr(34) & "{self.bat_file_path}" & Chr(34), 0\n'
                       f'Set WshShell = Nothing')

    def create_autorun(self) -> bool:
        self.__create_temp_files()
        SetValueEx(self.key_reg, AUTORUN_NAME, 0, REG_SZ, self.autorun_path)
        CloseKey(self.key_reg)
        return True

    def delete_autorun(self) -> bool:
        DeleteValue(self.key_reg, AUTORUN_NAME)
        os.remove(self.bat_file_path)
        os.remove(self.autorun_path)
        return True
