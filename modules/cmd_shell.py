import subprocess


class Shell:
    def __int__(self):
        pass

    @staticmethod
    def run_something(something: str) -> str:
        """
        Disclaimer:
        This module is used exclusively for educational purposes.
        I do not support and condemn any cybercrime.

        Remember about escaping characters.
        """
        return subprocess.check_output(something).decode("cp866", "ignore")
