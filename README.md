# RPI-Networking

all networking code to send our robot's video stream to a device as well as play music through a bluetooth speaker

## Steps
1. Install Python3 and required modules
2. Sign into the linkys network on your personal computer
3. Turn on the RPI, which autoconnects to the linksys network
4. SSH into the RPI using the following command: ssh pi@192.168.1.102 (password is password)
5. Make sure the config file has correct info.
6. To run the music and the camera broadcast on the RPI at the same time, run the `run.sh` command in your SSH connection. To exit these programs, press Ctrl+C twice.
7. To receive the camera broadcast from the RPI, run the `launchpad_recv.py` file on your personal computer
