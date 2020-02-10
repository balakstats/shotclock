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
        font = graphics.Font()
        font.LoadFont("/home/pi/Zeitnehmung/fonts/shotclockFonts/shotclockNumbers.bdf")
        textColorGreen = graphics.Color(255,255,0) # green
        textColorRed   = graphics.Color(255,0,0) # red

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        offset_canvas = self.matrix.CreateFrameCanvas()
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen, "--")
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

        print("wait for bluetooth connection")
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
        s.listen(backlog)
        print("Wait for bluetooth connection")
        client, address = s.accept()
        print("bluetooth connected")

        cool = True
        shotclockText = "--"

        while True:
            if cool:
                offscreen_canvas.Clear()
                if shotclockText == "--":
                    graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen, shotclockText)
                else:
                    graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen if int(shotclockText)>5 else textColorRed, shotclockText)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                cool = False

            try:
                data = client.recv(size)
            except Exception as ex:
                print("Lost bluetooth connection")
                offscreen_canvas.Clear()
                graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen, "--")
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
                cool = True
                recText = str(data).split("'")[1].strip("'")
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
