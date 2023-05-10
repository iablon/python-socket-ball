import tkinter as tk
import socket
import time

X=1
Y=1
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

root = tk.Tk()

root.title("Main Ball")
centerOffseth = root.winfo_screenheight()/2-400
centerOffsetw = root.winfo_screenwidth()/3-500
root.geometry("800x800+%d+%d" % (centerOffsetw, centerOffseth))

canvas = tk.Canvas(root, width=1600, height=800, confine=False)
canvas.pack() 

img = tk.PhotoImage(file="ball.png")
image = canvas.create_image(690, 100, image=img)

while True:
    time.sleep(0.004)

    if canvas.coords(image)[0]>=100:
        X=X-1
    if canvas.coords(image)[0]<=1495:
        X=X+1
    if canvas.coords(image)[1]>=100:
        Y=Y-1
    if canvas.coords(image)[1]<=700:
        Y=Y+1
    sock.sendto((str(canvas.coords(image)[0]+3)+","+str(canvas.coords(image)[1]-9)).encode(), ("127.0.0.1", 5005))
    print(str(canvas.coords(image)[0])+","+str(canvas.coords(image)[1]))
    canvas.move(image, X, Y)
    root.update()

