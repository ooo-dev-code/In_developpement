from tkinter import *

w = Tk()

w.geometry("780x780")
w.title("Graph")


    # can.create_line(x[0],470, x[1],fun[1], x[2],fun[2], x[3],fun[3], smooth=1)
    
# can.create_line(0,470, 100,50, 50,0, 0,50)

can = Canvas(w, bg="grey", width=770, height=470)
can.pack(expand=YES)

def function():
    x = [0, 5, 10, 15]
    fun = []
    for i in range(len(x)):
        f = (2*x[i]**2)+(2*x[i])+1
        fun.append(f)
    can.create_line(x[0],770, x[1],770-fun[1]-50, x[2],770-fun[2]-50, x[3],770-fun[3]-50, smooth=1, width=5)
    print(x, "     ", fun)

function()

w.mainloop()
