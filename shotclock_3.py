from samplebase import SampleBase
from rgbmatrix import graphics
import time
import socket
import subprocess

#TODO: create log file

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
#        super(SimpleSquare, self).__init__(*args, **kwargs)
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        # show initial value on shotclock
        font_1 = graphics.Font()
        font_1.LoadFont("/home/pi/shotclock/fonts/shotclockFonts/numbersSevenSegment.bdf")
        font_2 = graphics.Font()
        font_2.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf")
        textColorGreen = graphics.Color(255,255,0) # green
        textColorRed   = graphics.Color(255,0,0) # red

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        offset_canvas = self.matrix.CreateFrameCanvas()
#        offscreen_canvas.Clear()
#        graphics.DrawText(offscreen_canvas, font_1, 0, 31, textColorGreen, "0")
#        graphics.DrawText(offscreen_canvas, font_2, 32, 31, textColorGreen, "-")
#        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

#        print("wait for bluetooth connection")
#        cmd = "hciconfig"
#        device_id = "hci0"
#        status, output = subprocess.getstatusoutput(cmd)
#        bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
#        hostMACAddress = bt_mac
#        print(bt_mac)
#        port = 1
#        backlog = 1
#        size = 1024
#        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#        s.bind((hostMACAddress,port))
#        s.listen(backlog)
#        print("Wait for bluetooth connection")
#        client, address = s.accept()
#        print("bluetooth connected")

        cool = True
        cool = False
        shotclockText = "05"
        timeText      = "08:00"
        data = True
        while True:
            try:
                if cool:
                    if cool:
                        offscreen_canvas.Clear()
                        if shotclockText != "--":
                            print("if")
                            i = 0
                            for sh in shotclockText:
                                print(sh)
                                if sh in {"0","2","3","5","6","7","8","9"}: #segment a
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 23, textColorGreen, "0")
                                if sh in {"0","1","2","3","4","7","8","9"}: # segment b
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 24, textColorGreen, "1")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 18, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 20, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 30, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 32, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 26, textColorGreen, "2")
                                if sh in {"0","1","3","4","5","6","7","8","9"}: # segment c
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 38, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 40, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 34, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 36, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 46, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 48, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 12 if i==0 else 28, 41, textColorGreen, "1")
                                if sh in {"0","2","3","5","6","8","9"}: # segment d
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 43, textColorGreen, "0")
                                if sh in {"0","2","6","8"}: # segment e
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 38, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 40, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 34, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 36, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 46, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 48, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 41, textColorGreen, "1")
                                if sh in {"0","4","5","6","8","9"}: # segment f
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 24, textColorGreen, "1")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 18, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 20, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 30, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 32, textColorGreen, "2")
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 26, textColorGreen, "2")
                                if sh in {"2","3","4","5","6","8","9"}: # segment g
                                    graphics.DrawText(offscreen_canvas, font_1, 0 if i==0 else 16, 28, textColorGreen, "0")

                                i = i + 1
 #                       graphics.DrawText(offscreen_canvas, font_1, x, 48, textColorGreen, "1")
 #                       graphics.DrawText(offscreen_canvas, font_1, x, 36, textColorGreen, "1")
                        else:
                            print("else")
                            graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen if int(shotclockText)>5 else textColorRed, shotclockText)
                        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                        cool = False
#                    x=x+1
#                    y=y-1
            except:
                return

          #  try:
          #      data = client.recv(size)
          #  except Exception as ex:
          #      print("Lost bluetooth connection")
          #      offscreen_canvas.Clear()
          #      graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen, "--")
          #      offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
          #      print(ex)
          #      s.close()
          #      time.sleep(1)
          #      s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
          #      s.bind((hostMACAddress,port))
          #      s.listen(backlog)
          #      print("Wait for reconnect")
          #      client, address = s.accept()

            if data:
                cool = True
                data = False
#                recText = str(data).split("'")[1].strip("'")
                recText = "time%89"
                print(recText)
                recText = recText.split("#")
                try:
                    for text in recText:
                        print("text: "+text)
                        tempText = text.split("%")
                        if tempText[0] == "time":
                            shotclockText = tempText[1]
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
