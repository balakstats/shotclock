from samplebase import SampleBase
from rgbmatrix import graphics
import time
import sys
import socket
import subprocess

#from rgbmatrix import RGBMatrix, RGBMatrixOptions

#TODO: create log file

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
#        super(SimpleSquare, self).__init__(*args, **kwargs)
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        segments = 3
        f = open("/home/pi/shotclock/segments.txt","r")
        lines = f.readlines()
        line = lines[0].replace("\n","")
        print(line)
        segments = int(line)
        font_1 = graphics.Font()
        font_1.LoadFont("/home/pi/shotclock/fonts/shotclockFonts/numbersSevenSegment.bdf")
        font_2 = graphics.Font()
        font_2.LoadFont("/home/pi/shotclock/fonts/shotclockFonts/numbersSevenSegmentSmall.bdf")
        font_3 = graphics.Font()
        font_3.LoadFont("/home/pi/shotclock/fonts/shotclockFonts/numbersSevenSegmentNew_1.bdf")

        textColorGreen  = graphics.Color(255,255,0)  # green
        textColorRed    = graphics.Color(255,0,0)    # red
        textColorYellow = graphics.Color(0,255,255)  # yellow

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font_1, 0, 31, textColorGreen, "0")
        graphics.DrawText(offscreen_canvas, font_1, 16, 31, textColorGreen, "0")
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

        cmd            = "hciconfig"
        device_id      = "hci0"
        status, output = subprocess.getstatusoutput(cmd)

        bt_mac         = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
        hostMACAddress = bt_mac
        print(bt_mac)
        port    = 1
        backlog = 1
        size    = 1024
        s       = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((hostMACAddress,port))
        s.listen(backlog)
        print("Wait for bluetooth connection")
        client, address = s.accept()
        print("bluetooth connected")

        cool  = True
        short = 0
        shotclockText = "--"
        timeText      = "-:--"
        timeTextColor = textColorGreen
        shotclockTextColor = textColorGreen
        data = False
        while True:
            if cool:
                offscreen_canvas.Clear()
                cool = False
                if short>0:
                    print("short: "+str(short))
                    for loop in range(1,short+1):
                        if loop == 1:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 43, textColorYellow, "2")
                        elif loop == 2:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 48, textColorYellow, "2")
                        elif loop == 3:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 45, textColorYellow, "1")
                            graphics.DrawText(offscreen_canvas, font_1, 14, 36, textColorYellow, "1")
                        elif loop == 4:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 34, textColorYellow, "2")
                        elif loop == 5:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 39, textColorYellow, "2")
                        elif loop == 6:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 28, textColorYellow, "2")
                        elif loop == 7:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 25, textColorYellow, "1")
                            graphics.DrawText(offscreen_canvas, font_1, 14, 32, textColorYellow, "1")
                        elif loop == 8:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 30, textColorYellow, "2")
                        elif loop == 9:
                            graphics.DrawText(offscreen_canvas, font_1, 14, 19, textColorYellow, "2")
                short = 0
                if shotclockText != "--":
                    print("go 30")
                    color = textColorGreen if shotclockTextColor=="default" else textColorRed
                    i = 0
                    for sh in shotclockText:
                        if sh in {"0","2","3","5","6","7","8","9"}: #segment a
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 23, color, "0")
                        if sh in {"0","1","2","3","4","7","8","9"}: # segment b
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 24, color, "1")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 18, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 20, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 30, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 32, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 26, color, "2")
                        if sh in {"0","1","3","4","5","6","7","8","9"}: # segment c
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 38, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 40, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 34, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 36, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 46, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 48, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 41, color, "1")
                        if sh in {"2","3","4","5","6","8","9"}: # segment d
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 28, color, "0")
                        if sh in {"0","2","6","8"}: # segment e
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 38, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 40, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 34, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 36, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 46, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 48, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 41, color, "1")
                        if sh in {"0","4","5","6","8","9"}: # segment f
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 24, color, "1")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 18, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 20, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 30, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 32, color, "2")
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 26, color, "2")
                        if sh in {"0","2","3","5","6","8","9"}: # segment g
                            graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 43, color, "0")
                        i = i + 1
                else:
                    print("else --")
                    graphics.DrawText(offscreen_canvas, font_1,  0, 31, textColorGreen, "0")
                    graphics.DrawText(offscreen_canvas, font_1, 16, 31, textColorGreen, "0")
                if segments == 3:
                    if timeText != "-:--":
                        print("if 8:00")
                        i = 0
                        xH = 4
                        xV = 3
                        color = textColorGreen if timeTextColor=="default" else textColorRed
                        graphics.DrawText(offscreen_canvas, font_2, 11,  4, color, "2")  # draw the colon :
                        graphics.DrawText(offscreen_canvas, font_2, 11, 16, color, "2") # draw the colon :
                        for ti in timeText:
                            print(ti+": "+str(i))
                            xH = xH if i==0 else(15 if i==1 else 23)
                            xV = xV if i==0 else(14 if i==1 else 22)
                            if ti == ":":
                                continue
                            if ti in {"0","2","3","5","6","7","8","9"}: #segment a
                                graphics.DrawText(offscreen_canvas, font_2, xH,6, color, "0")
                            if ti in {"0","1","2","3","4","7","8","9"}: # segment b
                                graphics.DrawText(offscreen_canvas, font_2, xV+6, 8, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV+6, 2, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV+6, 3, color, "1")
                            if ti in {"0","1","3","4","5","6","7","8","9"}: # segment c
                                graphics.DrawText(offscreen_canvas, font_2, xV+6, 14, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV+6, 16, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV+6,  9, color, "1")
                            if ti in {"2","3","4","5","6","8","9"}: # segment d
                                graphics.DrawText(offscreen_canvas, font_2, xH,4, color, "0")
                            if ti in {"0","2","6","8"}: # segment e
                                graphics.DrawText(offscreen_canvas, font_2, xV, 14, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV, 16, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV,  9, color, "1")
                            if ti in {"0","4","5","6","8","9"}: # segment f
                                graphics.DrawText(offscreen_canvas, font_2, xV, 8, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV, 2, color, "2")
                                graphics.DrawText(offscreen_canvas, font_2, xV, 3, color, "1")
                            if ti in {"0","2","3","5","6","8","9"}: # segment g
                                graphics.DrawText(offscreen_canvas, font_2, xH,10, color, "0")

                            i = i + 1
                    else:
                        print("else --:--")
                        graphics.DrawText(offscreen_canvas, font_2, 2,  4, textColorGreen, "0")
                        graphics.DrawText(offscreen_canvas, font_2, 13, 4, textColorGreen, "0")
                        graphics.DrawText(offscreen_canvas, font_2, 21, 4, textColorGreen, "0")
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            try:
                data = client.recv(size)
            except Exception as ex:
                print("Lost bluetooth connection")
                offscreen_canvas.Clear()
                graphics.DrawText(offscreen_canvas, font_1,  0, 31, textColorGreen, "0")
                graphics.DrawText(offscreen_canvas, font_1, 16, 31, textColorGreen, "0")
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                print(ex)
                s.close()
                time.sleep(1)
                s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
                s.bind((hostMACAddress,port))
                s.listen(backlog)
                print("Wait for reconnect")
                client, address = s.accept()

            if data:
                recText = str(data).split("'")[1].strip("'")
                recText = recText.split("#")
                try:
                    for text in recText:
                        if len(text)>0:
                            cool = True
                            print("text: "+text)
                            tempText = text.split("%")
                            if tempText[0] == "shotclock":
                                shotclockText      = tempText[1]
                                shotclockTextColor = tempText[2]
                                short              = int(tempText[3])
                            elif segments == 3 and tempText[0] == "time":
                                print("set timeText: "+tempText[1])
                                timeText = tempText[1]
                                timeTextColor = tempText[2]
                            elif tempText[0] == "brightness":
                                if (int(tempText[1]) > 0) and (int(tempText[1]) <= 100):
                                    try:
                                        self.matrix.brightness = int(tempText[1])
                                    except:
                                        print("Could not set brightness")
                except Exception as ex:
                    print("could not process message")
                    print(ex)


if __name__=="__main__":
    print("Start shotclock")
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
