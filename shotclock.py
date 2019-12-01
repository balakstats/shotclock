from samplebase import SampleBase
from rgbmatrix import graphics
import time
import socket

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
#        super(SimpleSquare, self).__init__(*args, **kwargs)
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        # bluetooth server
        print("wait for bluetooth connection")
        hostMACAddress = "B8:27:EB:25:33:99"
        port = 1
        backlog = 1
        size = 1024
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((hostMACAddress,port))
        s.listen(backlog)
        client, address = s.accept()
        print("bluetooth connected")

        offset_canvas = self.matrix.CreateFrameCanvas()
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/Zeitnehmung/fonts/shotclockNumbers.bdf")
        textColor = graphics.Color(255,255,0)
        i = 0

        while True:
            data = client.recv(size)
           # for i in range(32):
            #    for j in range(32):
           # offset_canvas.Clear()
           # offscreen_canvas.Clear()
#            offset_canvas.Clear()
            offset_canvas.SetPixel(0,0,255,0,255)
#            offset_canvas.SetPixel(0,15,255,0,255)
#            offset_canvas.SetPixel(20,20,255,0,255)
#            offset_canvas.SetPixel(31,31,255,0,255)
               #     time.sleep(0.1)
#                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
#            text = ["00","11","22","33","44","55","66","77","88","99"]
 #           i = i+1
#            if i == 1:
            if data:
                print(str(data))
                text = str(data).split("'")[1].strip("'")
                print(text)
                offscreen_canvas.Clear()
                graphics.DrawText(offscreen_canvas, font, 0, 31, textColor, text)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
           # offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

#            time.sleep(0.5)


if __name__=="__main__":
  #  simple_square=SimpleSquare()
#    if(not simple_square.process()):
 #       simple_square.print_help()
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
