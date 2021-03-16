from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import ttk


def do_nothing():
    filewin = Toplevel(root)
    filewin.title('About')
    button = Button(filewin, text="Do nothing button")
    button.pack()


def load_filters():
    label = Label(root, text="Choose any filter to start")
    label.pack(pady=5)
    frame = Frame(root)
    filters = ['Average filter', 'Contrast stertching', 'histogram equalization', 'median filter']
    for x in range(len(filters)):
        btn = Button(frame, text=filters[x])
        btn.grid(row=0, column=x, padx=2)
    frame.pack()


def pick_image():
    for child in root.winfo_children():
        if not isinstance(child, Menu):
            child.destroy()
    global path
    path = askopenfilename()
    print(path)
    if len(path) > 0:
        try:
            image = Image.open(path)
            image = image.resize((200, 200))
            my_img = ImageTk.PhotoImage(image)
            global la
            la.destroy()
            label = Label(root, text="Chosen image")
            label.pack(pady=(5, 0))
            la = Label(root, image=my_img, width=200, height=200, borderwidth=1, relief="solid")
            la.image = my_img
            la.pack(pady=(5, 10))
            separator = ttk.Separator(root, orient='horizontal')
            separator.pack(fill='x')
            load_filters()
        except:
            la = Label(root, text="Please choose a valid image!")
            la.pack(pady=10)
    else:
        la = Label(root, text="Click File and choose open to open an image")
        la.pack(pady=10)


def create_menu():
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=pick_image)
    filemenu.add_command(label="Save", command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Description", command=do_nothing)
    helpmenu.add_command(label="Who coded it?", command=do_nothing)
    menubar.add_cascade(label="About", menu=helpmenu)

    root.config(menu=menubar)


root = Tk()
root.title('Image processing project')
root.geometry('900x600')
path = ''

###############
#             #
# Design here #
#             #
###############
create_menu()
la = Label(root, text="Click File and choose open to open an image")
la.pack(pady=10)

# Start rendering the application
root.mainloop()
