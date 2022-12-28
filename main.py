from tkinter import Toplevel, Button, Label, Frame, Menu, Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import ttk
from functools import partial
from average_filter import average_filter
from contrast_streching import contrast_stretching
from histogram_equilization import histo_eq
from median_filtering import median_filter
import cv2


# Global variables
root = Tk()
path = ""
img_label = Label()
la = Label()
img_name = ""


def do_nothing():
    filewin = Toplevel(root)
    filewin.title("About")
    button = Button(filewin, text="Do nothing button")
    button.pack()


def get_image_name():
    global img_name
    img_name = path.split("/")[-1]


def show_filter(func):
    global img_label
    img_label.destroy()
    img = cv2.imread(path, 0)
    img = func(img, img_name)
    cv2.imwrite(f"EditedImages/last_filter_{img_name}", img)
    img = Image.open(f"EditedImages/last_filter_{img_name}")
    image = img.resize((200, 200))
    my_img = ImageTk.PhotoImage(image)
    img_label = Label(
        root, image=my_img, width=200, height=200, borderwidth=1, relief="solid"
    )
    img_label.image = my_img
    img_label.pack(pady=20)


def load_filters():
    label = Label(root, text="Choose any filter to start")
    label.pack(pady=5)
    frame = Frame(root)
    filters = [
        "Average Filter",
        "Contrast Stertching",
        "Histogram Equalization",
        "Median Filter",
    ]
    functions = [average_filter, contrast_stretching, histo_eq, median_filter]
    for x in range(len(filters)):
        btn = Button(frame, text=filters[x], command=partial(show_filter, functions[x]))
        btn.grid(row=0, column=x, padx=2)
    frame.pack()


def clear_screen():
    for child in root.winfo_children():
        if not isinstance(child, Menu):
            child.destroy()


def pick_image():
    clear_screen()
    global path
    path = askopenfilename()
    if len(path) > 0:
        try:
            image = Image.open(path)
            image = image.resize((200, 200))
            my_img = ImageTk.PhotoImage(image)
            global la
            la.destroy()
            label = Label(root, text="Chosen image")
            label.pack(pady=(5, 0))
            la = Label(
                root, image=my_img, width=200, height=200, borderwidth=1, relief="solid"
            )
            la.image = my_img
            la.pack(pady=(5, 10))
            separator = ttk.Separator(root, orient="horizontal")
            separator.pack(fill="x")
            get_image_name()
            load_filters()
        except Exception:
            la = Label(root, text="Please choose a valid image!")
            la.pack(pady=10)
    else:
        la = Label(root, text="Click File and choose open to open an image")
        la.pack(pady=10)


def create_menu():
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=pick_image)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Description", command=do_nothing)
    menubar.add_cascade(label="About", menu=helpmenu)

    root.config(menu=menubar)


def main():
    root.title("Image Processing Project")
    root.geometry("900x600")
    ###############
    #             #
    # Design here #
    #             #
    ###############
    create_menu()
    global la
    la = Label(root, text="Click File and choose open to open an image")
    la.pack(pady=10)

    # Start rendering the application
    root.mainloop()


if __name__ == "__main__":
    main()
