from tkinter import *

num = 0

def Noter():
    print(password_entry.get())
    password = password_entry.get()
    label_titl2e = Label(frame, text=f"{password}", font=("Courrier, 40"))
    label_titl2e.pack()
    password_entry.delete(0, END)
    
def Noter_avec_un_bouton_car_on_a_mis_event(event):
    print(password_entry.get())
    password = password_entry.get()
    label_titl2e = Label(frame, text=f"{password}", font=("Courrier, 40"))
    label_titl2e.pack()
    password_entry.delete(0, END)
    

# Créer la fenêtre
window = Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background="orange")

frame = Frame(window, bg="white", highlightthickness=5, highlightbackground="black")
right_frame = Frame(window, bg="orange")

# Mot
label_title = Label(frame, text="Password", font=("Courrier, 40"))
label_title.pack()

# Écrire
password_entry = Entry(frame, font=("Courrier, 40"), bg="black", fg="white")
password_entry.pack()

# Butoon
yt_boutton = Button(frame, text="Noter",font=("Courrier, 23"), command=Noter)
yt_boutton.pack(pady=25, fill=X)

window.bind('<Escape>', Noter_avec_un_bouton_car_on_a_mis_event)

# Afficher
frame.pack(expand=YES)
window.mainloop()
