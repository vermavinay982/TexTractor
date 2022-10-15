from tkinter import *
from tkinter import filedialog
from functionality import *
from functools import partial
from PIL import Image,ImageTk

root = Tk()
root.title("TexTractor")
root.minsize(width=500,height=500)

# op_file = "images/code.png"

def browsefunc():
    filename =filedialog.askopenfilename(
        filetypes=(("video files","*.mp4"),("All files","*.*")))
    e_file.insert(END, filename)

def extract_text():
    global op_file
    file = e_file.get()
    search = e_search.get()
    print("File:",file,"Search:",search)
    find_text(file, search)
    callback()


l_file = Label(root, text="File")
e_file = Entry(root, width=30)
b_file = Button(root,text="Open File",command=browsefunc)
l_blank = Label(root, text=" ") 

l_file.grid(row=0, column=0, sticky=W, padx=50)
e_file.grid(row=0, column=1, sticky=E, padx=50)
b_file.grid(row=0, column=2)
l_blank.grid(row=2, column=0, sticky=W, padx=50)



def callback():
    img2 = ImageTk.PhotoImage(Image.open(op_file))
    panel.configure(image=img2)
    panel.image = img2

l_search = Label(root, text="Search") 
l_search.grid(row=1, column=0, sticky=W, padx=50)
e_search = Entry(root, width=30)
e_search.grid(row=1, column=1, sticky=E, padx=50)
b_text = Button(root, text="Extract Text", command=show)
b_slides = Button(root, text="Update Result",command=callback)
# b_find = Button(root, text="Find Text", command=partial(find_text, ("play") ))
b_find = Button(root, text="Find Text", command=extract_text)

b_text.grid(row = 3, column = 0, sticky = W,padx=50)
b_slides.grid(row = 3, column = 1, sticky = W,padx=90)
b_find.grid(row = 3, column = 2, sticky = W,padx=50)

# op_file = "images/code.png"
op_file = "images/output.png"
image = Image.open(op_file)
WIDTH, HEIGHT = 600,300
image = image.resize((WIDTH, HEIGHT))
photo = ImageTk.PhotoImage(image)
panel = Label(root, image = photo)
panel.place(anchor = CENTER, relx = 0.5, rely = .6)

root.mainloop()