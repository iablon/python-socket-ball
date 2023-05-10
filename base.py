import tkinter as tk

root = tk.Tk()
root.title("Ball movements")
centerOffseth = root.winfo_screenheight()/2-400
centerOffsetw = root.winfo_screenwidth()/3+400
root.geometry("800x800+%d+%d" % (centerOffsetw, centerOffseth))
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack() 
