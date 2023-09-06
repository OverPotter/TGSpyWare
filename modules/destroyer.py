import os
import subprocess
from config import BASE_DIR, DESTROYER_FILE_NAME


class Destroyer:
    def __int__(self):
        pass

    @staticmethod
    def delete_the_program():
        # first from venv
        interpreters = (subprocess.check_output("where python", shell=True).decode()).split()

        with open(DESTROYER_FILE_NAME, "w") as f:
            f.write("""
        import os
        os.system(f"rmdir /s /q {os.path.dirname(os.path.abspath(__file__))}")
            """)

        if len(interpreters) > 1:
            os.system(f"{interpreters[-1]} {os.path.join(BASE_DIR, DESTROYER_FILE_NAME)}")
