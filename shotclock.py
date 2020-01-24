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
        # bluetooth server
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

        offset_canvas = self.matrix.CreateFrameCanvas()
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/Zeitnehmung/fonts/shotclockFonts/shotclockNumbers.bdf")
        textColorGreen = graphics.Color(255,255,0) # green
        textColorRed   = graphics.Color(255,0,0) # red

        i = 0
        while True:
            try:
                data = client.recv(size)
            except Exception as ex:
                print("Lost bluetooth connection")
                print(ex)
                s.close()
                time.sleep(0.5)
                s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
                s.bind((hostMACAddress,port))
                s.listen(backlog)
                client, address = s.accept()
#            offset_canvas.SetPixel(0,0,255,0,255)

            try:
                if data:
                    print(str(data))
                    text = str(data).split("'")[1].strip("'")
                    print(text)
                    offscreen_canvas.Clear()
                    graphics.DrawText(offscreen_canvas, font, 0, 31, textColorGreen if int(text)>5 else textColorRed, text)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            except Exceptiopn as ex:
                print("could not process message")
                print(ex)
            time.sleep(0.3)

if __name__=="__main__":
  #  simple_square=SimpleSquare()
#    if(not simple_square.process()):
 #       simple_square.print_help()
    print("Start shotclock")
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
