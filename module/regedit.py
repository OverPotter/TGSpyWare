import os
from typing import TypeVar
from config import BASE_DIR, AUTORUN_NAME, RUN_FILENAME
from winreg import OpenKey, SetValueEx, DeleteValue, CloseKey, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ

# generic annotations
PyHKEY = TypeVar("PyHKEY")


class RegEdit:
    def __init__(self):
        self.autorun_path: str = os.path.join(BASE_DIR, RUN_FILENAME)
        self.key_reg: PyHKEY = OpenKey(HKEY_CURRENT_USER,
                                       r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                                       0, KEY_ALL_ACCESS)

    def create_autorun(self) -> None:
        SetValueEx(self.key_reg, AUTORUN_NAME, 0, REG_SZ, self.autorun_path)
        CloseKey(self.key_reg)

    def delete_autorun(self) -> None:
        DeleteValue(self.key_reg, AUTORUN_NAME)
