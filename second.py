import tkinter as tk
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5005))

root = tk.Tk()

root.title("Second Ball")
centerOffseth = root.winfo_screenheight()/2-400
centerOffsetw = root.winfo_screenwidth()/3+300
root.geometry("800x800+%d+%d" % (centerOffsetw, centerOffseth))

canvas = tk.Canvas(root, width=800, height=800, confine=False )
canvas.pack() 
coox=0
img = tk.PhotoImage(file="ball.png")
image = canvas.create_image(100, 100, image=img)
while True: 
    data, addr = sock.recvfrom(2048) 
    print(data.decode())
    if float(data.decode().split(",")[0])>700:
        canvas.itemconfigure(image, state="normal")
        coox=float(data.decode().split(",")[0])-970
        canvas.moveto(image, coox , float(data.decode().split(",")[1])-170)
    else:
        canvas.itemconfigure(image, state="hidden")
        coox=float(data.decode().split(",")[0])
        canvas.moveto(image, coox , float(data.decode().split(",")[1])-210)

    root.update()
