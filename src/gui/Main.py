
import tkinter as tk
import src.gui.Concrete
#from tkinter import Tk, Text, LEFT, TOP, RIGHT, BOTTOM, BOTH, RAISED, X, N
#from tkinter.ttk import Frame, Button, Style, Label, Entry

class GUI(tk.Frame):



    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master=master
        self.default_height=120
        self.config = src.gui.Concrete.Config()
        self.init_ui()

    def init_ui(self):
        self.init_position()
        self.init_controls()

    def init_position(self):
        self.master.title("Python Boids");
        self.pack(fill=tk.BOTH, expand=True)
        self.app_window = tk.Toplevel(self.master)
        self.app_frame = tk.Frame(self.app_window)
        self.app_window.overrideredirect(True)
        self.app_frame.pack()

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        self.ui_x = -7
        self.ui_y = 0

        self.config.set_size((sw,sh-self.default_height))

        self.master.geometry('%dx%d+%d+%d' % (sw, self.default_height, self.ui_x, self.ui_y))

    def init_controls(self):

        self.init_flock_frame()

    def init_flock_frame(self):


        frame_flock = tk.Frame(self, bd=2, relief=tk.GROOVE)
        frame_flock.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_settings = tk.Label(frame_flock, text="Flocks")
        label_flock_settings.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_list = tk.Frame(frame_flock, bd=1, relief=tk.RAISED)
        frame_flock_list.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        frame_flock_list_1 = tk.Frame(frame_flock_list)
        frame_flock_list_1.pack(side=tk.LEFT,padx=1)

        label_flock = tk.Label(frame_flock_list_1, text="Flock")
        label_flock.pack(side=tk.TOP, padx=5, pady=5)

        listbox_flocks_scrollbar = tk.Scrollbar(frame_flock_list_1,orient=tk.VERTICAL)
        listbox_flocks = tk.Listbox(frame_flock_list_1,yscrollcommand=listbox_flocks_scrollbar.set,name='listbox_flocks',height=1,width=16)
        #listbox_flocks_scrollbar.config(command=listbox_flocks_scrollbar.yview)
        listbox_flocks_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        listbox_flocks.pack(side=tk.TOP,fill=tk.Y)
        listbox_flocks.insert(tk.END, "0")
        listbox_flocks.insert(tk.END, "1")
        listbox_flocks.bind('<<ListboxSelect>>', GUI.on_select)

        frame_flock_list_2 = tk.Frame(frame_flock_list)
        frame_flock_list_2.pack(side=tk.LEFT,padx=1,fill=tk.BOTH)

        button_remove_flock = tk.Button(frame_flock_list_2,text="Remove Flock")
        button_remove_flock.pack(side=tk.BOTTOM,fill=tk.BOTH)

        button_add_flock = tk.Button(frame_flock_list_2, text="Add Flock")
        button_add_flock.pack(side=tk.BOTTOM, fill=tk.BOTH)

        frame_flock_size = tk.Frame(frame_flock, bd=1, relief=tk.RAISED)
        frame_flock_size.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_size = tk.Label(frame_flock_size, text="Size")
        label_flock_size.pack(side=tk.TOP, padx=5, pady=5)

        text_flock_size = tk.Text(frame_flock_size, height=1, width=2)
        text_flock_size.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_position = tk.Frame(frame_flock, bd=1, relief=tk.RAISED)
        frame_flock_position.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_position = tk.Label(frame_flock_position, text="Position")
        label_flock_position.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_position_1 = tk.Frame(frame_flock_position)
        frame_flock_position_1.pack(side=tk.TOP)

        label_flock_default_position_x = tk.Label(frame_flock_position_1, text="X: ")
        label_flock_default_position_x.pack(side=tk.LEFT, padx=5, pady=5)

        text_flock_default_position_x = tk.Text(frame_flock_position_1, height=1, width=4)
        text_flock_default_position_x.pack(side=tk.LEFT, padx=5, pady=5)

        label_flock_default_position_y = tk.Label(frame_flock_position_1, text="Y: ")
        label_flock_default_position_y.pack(side=tk.LEFT, padx=5, pady=5)

        text_flock_default_position_y = tk.Text(frame_flock_position_1, height=1, width=4)
        text_flock_default_position_y.pack(side=tk.LEFT, padx=5, pady=5)

        return frame_flock

    #def show(self):
    #    root = tk.Tk()
    #    root.resizable(0, 0)

    #    app = GUI(root)

    #    root.mainloop()

    def on_select(evt):
        w=evt.widget
        index=int(w.curselection()[0])
        value=w.get(index)
        r = value

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(0, 0)

    app = GUI(root)

    root.mainloop()