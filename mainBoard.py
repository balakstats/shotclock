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
        cmd = "hciconfig"
        device_id = "hci0"
        status, output = subprocess.getstatusoutput(cmd)
        bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
#        hostMACAddress = "B8:27:EB:25:33:99"
        hostMACAddress = bt_mac
        print(bt_mac)
        port = 2
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
#        font.LoadFont("/home/pi/Zeitnehmung/fonts/shotclockNumbers.bdf")
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x14.bdf")
        font1 = graphics.Font()
        font1.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")
        textColor = graphics.Color(255,255,0)
        textColor2 = graphics.Color(255,0,0)
        i = 0
        x=0
        y=0
        text1= " 1:"
        text2= " 2:"
        text3= " 3:"
        text4= " 4:"
        text5= " 5:"
        text6= " 6:"
        text7= " 7:"
        text8= " 8:"
        text9= " 9:"
        text10="10:"
        text11="11:"
        text12="12:"
        text13="13:"
        textS="*"
#        text4="4: ***"
#        text4="4: ***"
#        text4="4: ***"
  #      offscreen_canvas.Clear()
        print("Draw!")
   #     offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        textT="-:-"
        textR="-:-"
        while True:
            offscreen_canvas.Clear()
#            graphics.DrawText(offscreen_canvas, font,  0, 15, textColor, text2)
 #           graphics.DrawText(offscreen_canvas, font,  0, 0, textColor, text3)
    #        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
#            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            graphics.DrawText(offscreen_canvas, font1, 192,  5, textColor, text1)
            graphics.DrawText(offscreen_canvas, font1, 192, 11, textColor, text2)
            graphics.DrawText(offscreen_canvas, font1, 192, 17, textColor, text3)
            graphics.DrawText(offscreen_canvas, font1, 208, 17, textColor2, textS)
            graphics.DrawText(offscreen_canvas, font1, 212, 17, textColor2, textS)
            graphics.DrawText(offscreen_canvas, font1, 192, 23, textColor, text4)
            graphics.DrawText(offscreen_canvas, font1, 192, 29, textColor, text5)
            graphics.DrawText(offscreen_canvas, font1,   0,  5, textColor, text6)
            graphics.DrawText(offscreen_canvas, font1,   0, 11, textColor, text7)
            graphics.DrawText(offscreen_canvas, font1,   0, 17, textColor, text8)
            graphics.DrawText(offscreen_canvas, font1,   0, 23, textColor, text9)
            graphics.DrawText(offscreen_canvas, font1,   0, 29, textColor, text10)
            graphics.DrawText(offscreen_canvas, font1,   16, 29, textColor2, textS)
            graphics.DrawText(offscreen_canvas, font1,   224, 5, textColor, text11)
            graphics.DrawText(offscreen_canvas, font1,   224, 11, textColor, text12)
            graphics.DrawText(offscreen_canvas, font1,   224, 17, textColor2, text13)
            graphics.DrawText(offscreen_canvas, font1,   240, 17, textColor2, textS)
            graphics.DrawText(offscreen_canvas, font1,   244, 17, textColor2, textS)
            graphics.DrawText(offscreen_canvas, font1,   248, 17, textColor2, textS)


            graphics.DrawText(offscreen_canvas, font1, 321,  5, textColor, text1)
            graphics.DrawText(offscreen_canvas, font1, 321, 11, textColor, text2)
            graphics.DrawText(offscreen_canvas, font1, 321, 17, textColor, text3)
            graphics.DrawText(offscreen_canvas, font1, 321, 23, textColor, text4)
            graphics.DrawText(offscreen_canvas, font1, 321, 29, textColor, text5)
            graphics.DrawText(offscreen_canvas, font1, 129,  5, textColor, text6)
            graphics.DrawText(offscreen_canvas, font1, 129, 11, textColor, text7)
            graphics.DrawText(offscreen_canvas, font1, 129, 17, textColor, text8)
            graphics.DrawText(offscreen_canvas, font1, 129, 23, textColor, text9)
            graphics.DrawText(offscreen_canvas, font1, 129, 29, textColor, text10)
            graphics.DrawText(offscreen_canvas, font1, 353,  5, textColor, text11)
            graphics.DrawText(offscreen_canvas, font1, 353, 11, textColor, text12)
            graphics.DrawText(offscreen_canvas, font1, 353, 17, textColor, text13)
            
 #           graphics.DrawText(offscreen_canvas, font1, 192, 21, textColor, text4)
 #           graphics.DrawText(offscreen_canvas, font1, 192, 21, textColor, text4)
 #           graphics.DrawText(offscreen_canvas, font1, 192, 21, textColor, text4)

            graphics.DrawText(offscreen_canvas, font, 260, 31, textColor, textT)
            graphics.DrawText(offscreen_canvas, font, 68, 31, textColor, textR)

#            offscreen_canvas.SetPixel(0,0,255,0,255)
#            x=x+1
#            if x==64:
#                x=0


            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            data = client.recv(size)
           # for i in range(32):
            #    for j in range(32):
           # offset_canvas.Clear()
#            offscreen_canvas.Clear()
#            offset_canvas.Clear() 
#            offset_canvas.SetPixel(0,15,255,0,255)
#            offset_canvas.SetPixel(20,20,255,0,255)
#            offset_canvas.SetPixel(31,31,255,0,255)
               #     time.sleep(0.1)
#             offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
  #          text = ["00","11","22","33","44","55","66","77","88","99"]
 #           i = i+1
#            if i == 1:
            if data:
    #        if True:
                print(str(data))
                textT = str(data).split("'")[1].strip("'").split("#")[0]
                textR = str(data).split("'")[1].strip("'").split("#")[1]
#                print(text)
#                text = "AAAAAABBB"
#                offscreen_canvas.Clear()
#                graphics.DrawText(offscreen_canvas, font, 80, 15, textColor, text)
#                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(0.1)


if __name__=="__main__":
  #  simple_square=SimpleSquare()
#    if(not simple_square.process()):
 #       simple_square.print_help()
#    while True:
#    try:
    print("Start shotclock")
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
 #   except:
  #      print("Lost connection")
   #     time.sleep(5)
