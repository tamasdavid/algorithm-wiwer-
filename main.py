from tkinter import *


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("comicsans", "9", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


window = Tk()
window.title("Algorithm Viewer")
# positioning the window to the middle of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 600
height = 400
x_coordinate = int((screen_width / 2) - (width / 2))
y_coordinate = int((screen_height / 2) - (height / 2))
window.config(padx=20, pady=15)
window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
window.resizable(0, 0)

# buttons to open the algorithm viewer and add the description of the algorithm in tooltip
bouble_sort_btn = Button(window, text="Bubble Sort", width=12, bg="lightgreen", font=("Comicsans", 12))
CreateToolTip(bouble_sort_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
bouble_sort_btn.grid(row=0, column=1)

selection_sort_btn = Button(window, text="Selection Sort", width=12, bg="#5686DA", font=("Comicsans", 12))
CreateToolTip(selection_sort_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
selection_sort_btn.grid(row=1, column=0)

insertion_sort_btn = Button(window, text="Insertion Sort", width=12, bg="violet", font=("Comicsans", 12))
CreateToolTip(insertion_sort_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
insertion_sort_btn.grid(row=1, column=2)

shell_sort_btn = Button(window, text="Shell Sort", width=12, bg="yellow", font=("Comicsans", 12))
CreateToolTip(shell_sort_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
shell_sort_btn.grid(row=2, column=1)

merge_sort_btn = Button(window, text="Merge Sort", width=12, bg="pink", font=("Comicsans", 12))
CreateToolTip(merge_sort_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
merge_sort_btn.grid(row=3, column=0)

quick_sort_btn = Button(window, text="Quick Sort", width=12, bg="orange", font=("Comicsans", 12))
CreateToolTip(quick_sort_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
quick_sort_btn.grid(row=3, column=2)

a_path_finding_btn = Button(window, text="A Path Finding Algorithm", bg="#B1D4D5", font=("Comicsans", 12))
CreateToolTip(a_path_finding_btn, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
a_path_finding_btn.grid(row=4, column=1)


window.mainloop()



