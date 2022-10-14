from tkinter import *

root = Tk()
root.title("TexTractor")
root.minsize(width=500,height=500)

l_file = Label(root, text="File")
e_file = Entry(root, show="File Path", )
l_file.pack(anchor=W)
e_file.pack(anchor=E)

l_search = Label(root, text="Search")
l_search.pack(anchor=W)
e_search = Entry(root, show="Text Search")
e_search.pack(anchor=E)

l_skip = Label(root, text="Skip")
l_skip.pack(anchor=W)
s_skip = Spinbox(root, from_=1, to=40)
s_skip.pack(anchor=E)
# e_skip = Entry(root, show="Skip Frames")
# e_skip.pack()



b_text = Button(root, text="Extract Text")
b_slides = Button(root, text="Create Slides")
b_find = Button(root, text="Find Text")

b_text.pack()
b_slides.pack()
b_find.pack()

root.mainloop()