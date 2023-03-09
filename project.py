from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os

root=Tk()

root.title("My First App")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="yellow")

open_img = ImageTk.PhotoImage(Image.open("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open("save_file.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))


label_file_name = Label(root,text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor = CENTER)

my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)


name = ""
def openfile():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file = filedialog.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    name = os.path.basename(text_file)
    formated_name  = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()

open_button = Button(root,image=open_img,text="Open File")
open_button.place(relx=0.05,rely=0.03,anchor = CENTER)

save_button = Button(root,image=save_img,text="Save File")
save_button.place(relx=0.11,rely=0.03,anchor = CENTER)

run_button = Button(root,image=run_img,text="Run")
run_button.place(relx=0.17,rely=0.03,anchor = CENTER)
root.mainloop()
