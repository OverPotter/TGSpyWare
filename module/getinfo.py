import psutil
import platform
import socket
import getpass
from datetime import datetime
from uuid import getnode as get_mac
from speedtest import Speedtest


class GetInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_pc_info():
        username = getpass.getuser()
        ip = socket.gethostbyname(socket.gethostname())
        mac = get_mac()
        os_info = platform.uname()
        zone = psutil.boot_time()
        os_time = datetime.fromtimestamp(zone)
        cpu_data = psutil.cpu_freq()

        result = (f"Operating System: {os_info.system}\n"
                  f"Processor: {os_info.processor}\n"
                  f"Username: {username}\n  IP adress: {ip}\n"
                  f"MAC address: {mac}\n"
                  f"Timezone: {os_time.year}/{os_time.month}/{os_time.day}"
                  f" {os_time.hour}:{os_time.minute}:{os_time.second}\n"
                  f"Max Frequency: {cpu_data.max:.2f} Mhz\n"
                  f"Min Frequency: {cpu_data.min:.2f} Mhz\n"
                  f"Current Frequency: {cpu_data.current:.2f} Mhz\n")

        return result

    @staticmethod
    def get_connection_info():
        start = datetime.now()
        inet = Speedtest()

        download_speed = float(f"{str(inet.download())[0:2]}.{str(round(inet.download(), 2))[1]}") * 0.125
        upload_speed = float(f"{str(inet.upload())[0:2]}.{str(round(inet.download(), 2))[1]}") * 0.125

        ends = datetime.now()
        work_speed = format(ends - start)

        result = (f"Work speed: {work_speed}\n"
                  f"Download: {download_speed} MB/s\n"
                  f"Upload: {upload_speed} MB/s\n")

        return result
