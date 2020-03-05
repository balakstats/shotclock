#!/bin/sh
sleep 10
sudo python3 /home/pi/Zeitnehmung/shotclock.py --led-brightness=10 --led-rows=16 --led-cols=32 --led-multiplexing=4 --led-parallel=3
