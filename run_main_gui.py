from tkinter import *
from tkinter import filedialog
from functionality import *
from functools import partial
from PIL import Image,ImageTk

root = Tk()
root.title("TexTractor")
root.minsize(width=500,height=500)

global ctr
ctr = 0

WIDTH, HEIGHT = 500,250
logo_file = "assets/textractor_logo.png"

def browsefunc():
    global ctr
    ctr = 0
    e_file.delete(0, END)
    filename =filedialog.askopenfilename(
        filetypes=(("video files","*.mp4"),("All files","*.*")))
    e_file.insert(END, filename)

def search_text(debug=False):
    global ctr

    file = e_file.get()
    search = e_search.get()

    result_file, ctr = find_text(file, search, ctr, debug)
    callback(result_file)
    print(f"File:{file},Search:{search},Result:{result_file} at {ctr}" )

def extract_text(debug=False):
    file = e_file.get()
    result_file, text = extract_video_text(file, debug)
    print(f"File:{file},Result:{result_file} at {ctr}" )

def callback(op_file=None):
    if op_file is None:
        op_file = logo_file
    image = Image.open(op_file)
    image = image.resize((WIDTH, HEIGHT))
    image = ImageTk.PhotoImage(image)
    
    panel.configure(image=image)
    panel.image = image

def reset():
    global ctr
    ctr = 0
    callback()

l_file = Label(root, text="File")
l_file.grid(row=0, column=0, sticky=W, padx=50)

e_file = Entry(root, width=30)
e_file.grid(row=0, column=1, sticky=E, padx=50)

b_file = Button(root,text="Open File",command=browsefunc)
b_file.grid(row=0, column=2)

l_blank = Label(root, text=" ") 
l_blank.grid(row=2, column=0, sticky=W, padx=50)

l_search = Label(root, text="Search") 
l_search.grid(row=1, column=0, sticky=W, padx=50)

e_search = Entry(root, width=30)
e_search.grid(row=1, column=1, sticky=E, padx=50)

b_text = Button(root, text="Extract Text", command=extract_text)
b_text.grid(row = 3, column = 0, sticky = W,padx=50)

b_find = Button(root, text="Find Text", command=search_text)
b_find.grid(row = 3, column = 1, sticky = W,padx=90)

b_reset = Button(root, text="Reset",command=reset)
b_reset.grid(row = 3, column = 2, sticky = W,padx=50)
# b_find = Button(root, text="Find Text", command=partial(find_text, ("play") ))

image = Image.open(logo_file)
image = image.resize((WIDTH, HEIGHT))
photo = ImageTk.PhotoImage(image)

panel = Label(root, image = photo)
panel.place(anchor = CENTER, relx = 0.5, rely = .6)

root.mainloop()