import os
import time
import subprocess
from datetime import datetime
from config import TASK_NAME, DESTROYER_FILENAME, BASE_DIR


class Destroyer:
    def __int__(self):
        pass

    @staticmethod
    def __create_file_destroyer():
        with open(DESTROYER_FILENAME, "w") as f:
            f.write(f"@echo off\n"
                    f"SCHTASKS /Delete /TN {TASK_NAME} /F\n"
                    f"rmdir /s /q {BASE_DIR}")

    def delete_the_program(self):
        self.__create_file_destroyer()

        unix_timestamp = time.time() + 60
        scheduled_time = datetime.fromtimestamp(unix_timestamp).strftime("%H:%M")

        subprocess.run(rf"SCHTASKS /Create /SC ONCE /ST {scheduled_time} /F /TN {TASK_NAME} /TR {os.path.join(BASE_DIR, DESTROYER_FILENAME)}")
