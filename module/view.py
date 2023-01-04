import cv2
import pyautogui
from config import SCREENSHOT_PATH, WEBCAM_SCREEN_PATH


class View:
    def __int__(self):
        pass

    @staticmethod
    def make_screenshot() -> str:
        pyautogui.screenshot(SCREENSHOT_PATH)
        return SCREENSHOT_PATH

    @staticmethod
    def make_webcam_screen() -> str:
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()

        ret, frame = cap.read()
        cv2.imwrite(WEBCAM_SCREEN_PATH, frame)
        cap.release()
        return WEBCAM_SCREEN_PATH
