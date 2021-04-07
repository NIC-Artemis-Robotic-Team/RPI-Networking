#!/usr/bin/env python3

import configparser, subprocess, os

config_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.dirname(config_path)

config = configparser.ConfigParser()
config.read(f"{config_path}/config.ini")
fileName = config['Audio']['fileName']
volume = config['Audio']['volume']
fileName = config_path + "/" + fileName

print(f"Playing {fileName}...")

try:
    subprocess.run(f"ffplay -loop 0 -volume {volume} -nodisp {fileName}".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except KeyboardInterrupt:
    print(f"Done playing {fileName}!")
