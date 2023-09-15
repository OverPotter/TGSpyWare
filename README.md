# Monitoring System (SpyWare) with a C2 server based on a chatbot in telegram
This software allows you to monitor the operation of your (and not only your) computer and remotely control it using telegram as a C2 server.

![](https://img.shields.io/badge/python-3.9-blueviolet)
![](https://img.shields.io/github/last-commit/OverPotter/TGSpyWare?color=blueviolet)
![](https://img.shields.io/github/issues-pr/OverPotter/TGSpyWare?color=blueviolet)
![](https://img.shields.io/github/forks/OverPotter/TGSpyWare?style=social)
---
## Disclaimer
Attention! The author of this software is not responsible for any consequences from its use. 
All materials are provided exclusively for educational purposes!
___
## Installation
Use the git to install SpyWare.
```bash
git clone https://github.com/OverPotter/TGSpyWare.git
```
---
## Current functionality:
- /check - Checking System Status
- /pc_info - System characteristics
- /con_info - Connection characteristics
- /proc_info - List of running processes
- /wifi_info - Information about Wi-Fi connections
- /pub_ip_info - Information about public IP address
- /screen - Desktop screenshot
- /webcam_screen - Webcam screen
- /audio n - (n - count of seconds)Record sound from voice recorder for 5 seconds by default
- /exec c - (c - command) Execute command in cmd
- /reg_autorun - Append programme to registry
- /del_autorun - Delete programme from registry
- /exit - Shutting down the program before reboot
- /destroy - Delete the program from the computer
---
## Launching
To launch, you need to create a bot via [@BotFather](https://t.me/BotFather ), get our ID in telegram via [@IDBot](https://t.me/username_to_id_bot ) or [@userinfobot](https://t.me/userinfobot )
after fill in `tg_config.py ` and launch `main.py `.
___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
___ 
## License
[MIT](https://choosealicense.com/licenses/mit/)
