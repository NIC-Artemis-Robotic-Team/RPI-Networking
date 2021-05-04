#!/usr/bin/env python3

import configparser, subprocess, os

config_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.dirname(config_path)

config = configparser.ConfigParser()
config.read(f"{config_path}/config.ini")
fileName = config['Audio']['fileName']
volume = config['Audio']['volume']
macAddr = config['Audio']['macAddr']

fileName = config_path + "/" + fileName

print(f"Connecting to {macAddr}...")
subprocess.run(f"bluetoothctl connect {macAddr}".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"Playing {fileName}...")
while True:
    try:
        subprocess.run(f"aplay -D={macAddr} {fileName}".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except KeyboardInterrupt:
        print(f"Done playing {fileName}!")
