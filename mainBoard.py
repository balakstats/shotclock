from samplebase import SampleBase
from rgbmatrix import graphics
import time
import socket
import subprocess
import sys

#import RPi.GPIO as gpio
#gpio.setmode(gpio.BCM)
#gpio.setup(6, gpio.OUT)
#gpio.output(6, gpio.HIGH)
#time.sleep(1)
#gpio.output(6, gpio.LOW)
#time.sleep(1)
#gpio.output(6, gpio.HIGH)
#time.sleep(1)
#gpio.output(6, gpio.LOW)



#TODO: create log file

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
#        super(SimpleSquare, self).__init__(*args, **kwargs)
        super(RunText, self).__init__(*args, **kwargs)
#        self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)


    def run(self):
        # start bluetooth server
        cmd = "hciconfig"
        device_id = "hci0"
        status, output = subprocess.getstatusoutput(cmd)
        bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
        hostMACAddress = bt_mac
        print(bt_mac)
        port = 1
        backlog = 1
        size = 1024
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((hostMACAddress,port))
        print("wait for bluetooth connection")
        s.listen(backlog)
        client, address = s.accept()
        print("bluetooth connected")

#        offset_canvas    = self.matrix.CreateFrameCanvas()
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/Zeitnehmung/fonts/mainBoardFonts/timeNumbers.bdf")
#        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf")
        font1 = graphics.Font()
        font1.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x7.bdf")
        textColor = graphics.Color(255,255,0)
        textColorRed = graphics.Color(255,0,0)
        textColorGreen = graphics.Color(0,255,0)
        textColorBlue = graphics.Color(25,25,255)
        textColorWhite = graphics.Color(255,255,255)

        player_blue = [{"X":192,"Y":8,"T":" 1:","A":0},{"X":192,"Y":15,"T":" 2:","A":0},{"X":192,"Y":22,"T":" 3:","A":0},{"X":192,"Y":29,"T":" 4:","A":0}
                      ,{"X":0,"Y":6,"T":" 5:","A":0},{"X":0,"Y":13,"T":" 6:","A":0},{"X":0,"Y":22,"T":" 7:","A":0},{"X":0,"Y":29,"T":" 8:","A":0}
                      ,{"X":224,"Y":8,"T":" 9:","A":0},{"X":224,"Y":15,"T":"10:","A":0},{"X":224,"Y":22,"T":"11:","A":0},{"X":224,"Y":29,"T":"12:","A":0}
                     ,{"X":32,"Y":6,"T":"13:","A":0}]

        player_white = [{"X":321,"Y":8,"T":" 1:","A":0},{"X":321,"Y":15,"T":" 2:","A":0},{"X":321,"Y":22,"T":" 3:","A":0},{"X":321,"Y":29,"T":" 4:","A":0}
                       ,{"X":129,"Y":6,"T":" 5:","A":0},{"X":129,"Y":13,"T":" 6:","A":0},{"X":129,"Y":22,"T":" 7:","A":0},{"X":129,"Y":29,"T":" 8:","A":0}
                       ,{"X":353,"Y":8,"T":" 9:","A":0},{"X":353,"Y":15,"T":"10:","A":0},{"X":353,"Y":22,"T":"11:","A":0},{"X":353,"Y":29,"T":"12:","A":0}
                       ,{"X":161,"Y":6,"T":"13:","A":0}]

        print("Draw!")
        textTime="-:-"
        textResult="-:-"
        textTeamBlue="---"
        textTeamWhite="---"

        while True:
            offscreen_canvas.Clear()
            i=0
            for player in player_blue:
                graphics.DrawText(offscreen_canvas, font1, player["X"], player["Y"], textColorBlue if player["A"]<3 else (textColorGreen if i==4 or i==5 or i==12 else textColorRed), player["T"])
                if player["A"] > 0:
                    graphics.DrawText(offscreen_canvas, font1, player["X"]+13, player["Y"], textColorGreen if i==4 or i==5 or i==12 else textColorRed, ("*" if player["A"]==1 else ("**" if player["A"]==2 else "***")))
                i=i+1

            i=0
            for player in player_white:
                graphics.DrawText(offscreen_canvas, font1, player["X"], player["Y"], textColorWhite if player["A"]<3 else (textColorGreen if i==4 or i==5 or i==12 else textColorRed), player["T"])
                if player["A"] > 0:
                    graphics.DrawText(offscreen_canvas, font1, player["X"]+13, player["Y"], textColorGreen if i==4 or i==5 or i==12 else textColorRed, ("*" if player["A"]==1 else ("**" if player["A"]==2 else "***")))
                i=i+1


            graphics.DrawText(offscreen_canvas, font, 253, 31, textColor, textTime)
            tempText = textResult.split(":")
            print(tempText[0])
            if (tempText[0] != "-") and (int(tempText[0]) > 9):
                x = 46
            else:
                x = 61
            graphics.DrawText(offscreen_canvas, font, x, 31, textColor, textResult)

            graphics.DrawText(offscreen_canvas, font1, 32, 29, textColor, textTeamBlue)
            graphics.DrawText(offscreen_canvas, font1, 161, 29, textColor, textTeamWhite)

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            try:
                data = client.recv(size)
            except:
                print("lost connection")
                time.sleep(5)
                s.close()
                time.sleep(1)
                s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
                s.bind((hostMACAddress,port))
                s.listen(backlog)
                client, address = s.accept()

            if data:
                recText = str(data).split("'")[1].strip("'")
                print(recText)
                recText = recText.split("#")
                try:
                    for text in recText:
                        print("text: "+text)
                        tempText = text.split("%")
                        if tempText[0] == "time":
                            textTime = tempText[1]
                            pause = False
                            timeout = False
                            print("time: "+textTime)
                        elif tempText[0] == "result":
                            textResult = tempText[1]
                            print("result: "+textResult)
                        elif tempText[0] == "player":
                            print(tempText[0])
                            print(tempText[1])
                            print(tempText[2])
                            print(tempText[3])
                            if tempText[1].lower() == "blue":
                                player_blue[int(tempText[2])-1]["A"] = int(tempText[3])
                            else:
                                player_white[int(tempText[2])-1]["A"] = int(tempText[3])
                        elif tempText[0] == "brightness":
                            if int(tempText[1]) > 0 and int(tempText[1]) <= 100:
                                print("brightness: "+tempText[1])
                                try:
                                    self.matrix.brightness = int(tempText[1])
                                except:
                                    print("could not set brightness")
                        elif tempText[0] == "pause":
                            pause = True
                        elif tempText[0] == "timeout":
                            timeout = True
                        elif tempText[0] == "teamBlue":
                            textTeamBlue = tempText[1]
                            print("yes blue")
                        elif tempText[0] == "teamWhite":
                            textTeamWhite = tempText[1]
                            print("yes white")
                except:
                    print("could not process message")
#                    if "brightness%*" in 

 #           time.sleep(0.05)


if __name__=="__main__":
  #  simple_square=SimpleSquare()
#    if(not simple_square.process()):
 #       simple_square.print_help()
    while True:
        try:
            print("Start shotclock")
            run_text = RunText()
            time.sleep(3)
            if (not run_text.process()):
                run_text.print_help()
        except Exception as ex:
            print(ex)
            time.sleep(3)
