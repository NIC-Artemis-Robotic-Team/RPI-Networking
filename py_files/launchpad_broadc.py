#!/usr/bin/env python3

import sys
import time
import os
import configparser
import socket
import traceback
from time import sleep
import cv2
from imutils.video import VideoStream
import imagezmq

def main():
    config_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.dirname(config_path)
    config = configparser.ConfigParser()
    config.read(f"{config_path}/config.ini")

    port = int(config['Camera']['portNumber'])
    frame_rate = int(config['Camera']['frameRate'])
    # ranges from 0-100
    jpeg_quality = int(config['Camera']['jpegQuality'])

    sender = imagezmq.ImageSender("tcp://*:{}".format(port), REQ_REP=False)
    capture = VideoStream(usePiCamera=True)  # PiCamera
    capture.start()

    sleep(2.0)  # Warmup time; needed by PiCamera on some RPi's
    print("Input stream opened")
    prev = 0
    rpi_name = socket.gethostname()
    try:
        counter = 0
        while True:
            time_elapsed = time.time() - prev
            frame = capture.read()
            if time_elapsed > 1.0/frame_rate and frame.all() != None:
                prev = time.time()
                ret_code, jpg_buffer = cv2.imencode(
                    ".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
                sender.send_jpg(rpi_name, jpg_buffer)

            counter = counter + 1
    except (KeyboardInterrupt, SystemExit):
        print('Exit due to keyboard interrupt')
    except Exception as ex:
        print('Python error with no Exception handler:')
        print('Traceback error:', ex)
        traceback.print_exc()
    finally:
        capture.stop()
        sender.close()
        sys.exit()


if __name__ == "__main__":
    main()

