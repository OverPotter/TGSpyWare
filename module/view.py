import pyautogui
from config import SCREENSHOT_PATH


class View:
    def __int__(self):
        pass

    @staticmethod
    def make_screenshot():
        pyautogui.screenshot(SCREENSHOT_PATH)
        return SCREENSHOT_PATH
