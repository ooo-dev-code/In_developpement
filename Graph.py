from tkinter import *

width = 1080
height = 780

w = Tk()

w.geometry(f"{width}x{height}")
w.title("Graph")

can = Canvas(w, bg="grey", width=width, height=height)
can.pack(expand=YES)

# Make the Graph

can.create_line(width/2,height, width/2,height/2, width/2,0, width/2,height, width=3)
can.create_line(width,height/2, width/2,height/2, 0,height/2, width,height/2, width=3)

for i in range(0, width, 20):
    can.create_line(i,height/2-5, i,height/2, i,height/2, i,height/2+5, width=1)
for i in range(0, height, 20):
    can.create_line(width/2-5,i, width/2,i, width/2,i, width/2+5,i, width=1)

def Function():
    x = [0, 10, 20, 30]
    function = []
    for i in range(len(x)):
        f = x[i]**2
        function.append(f)
    can.create_line(x[0]+width/2,height/2-function[0], x[1]+width/2,height/2-function[1], x[2]+width/2,height/2-function[2], x[3]+width/2,height/2-function[3], smooth=1, width=2, fill="blue")
    
    neg_x = [0, -10, -20, -30]
    neg_function = []
    for i in range(len(neg_x)):
        neg_f = neg_x[i]**2
        neg_function.append(neg_f)
    can.create_line(neg_x[0]+width/2,height/2-neg_function[0], neg_x[1]+width/2,height/2-neg_function[1], neg_x[2]+width/2,height/2-neg_function[2], neg_x[3]+width/2,height/2-neg_function[3], smooth=1, width=2, fill="blue")
    
    print(function, x)

Function()

w.mainloop()
