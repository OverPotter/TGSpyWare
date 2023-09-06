import subprocess


class Shell:
    def __int__(self):
        pass

    @staticmethod
    def exec_command(command):
        subprocess.call(command)
