import cv2
import win32api
import win32con
import win32gui
import win32ui
from PIL import Image
from config import SCREENSHOT_PATH, WEBCAM_SCREEN_PATH


class View:
    def __int__(self):
        pass

    @staticmethod
    def __get_dimensions():
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        return width, height, left, top

    def make_screenshot(self):
        hdesktop = win32gui.GetDesktopWindow()
        width, height, left, top = self.__get_dimensions()

        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()

        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        mem_dc.SelectObject(screenshot)
        mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

        bmp_info = screenshot.GetInfo()
        bmp_str = screenshot.GetBitmapBits(True)
        img = Image.frombuffer(
            'RGB',
            (bmp_info['bmWidth'], bmp_info['bmHeight']),
            bmp_str, 'raw', 'BGRX', 0, 1)
        img.save(f'{SCREENSHOT_PATH}.jpeg', 'jpeg')

        mem_dc.DeleteDC()
        win32gui.DeleteObject(screenshot.GetHandle())
        return f"{SCREENSHOT_PATH}.jpeg"

    @staticmethod
    def make_webcam_screen() -> str:
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()

        ret, frame = cap.read()
        cv2.imwrite(WEBCAM_SCREEN_PATH, frame)
        cap.release()
        return WEBCAM_SCREEN_PATH
