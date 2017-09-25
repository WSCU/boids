
import tkinter as tk
import UI.Concrete
#from tkinter import Tk, Text, LEFT, TOP, RIGHT, BOTTOM, BOTH, RAISED, X, N
#from tkinter.ttk import Frame, Button, Style, Label, Entry

class GUI(tk.Frame):



    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master=master
        self.default_height=120
        self.config = UI.Concrete.Config()
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




        #frame3 = tk.Frame(self)
        #frame3.pack(side=tk.LEFT, anchor=tk.N)

        #label_flock_position = tk.Label(frame3, text="Flock Position")
        #label_flock_position.pack(side=tk.LEFT, padx=5, pady=5)

        #entry_flock_position_x = tk.Entry(frame3)
        #entry_flock_position_x.pack(side=tk.LEFT,padx=5, pady=5)

        #entry_flock_position_y = tk.Entry(frame3)
        #entry_flock_position_y.pack(side=tk.LEFT,padx=5, pady=5)

    def init_flock_frame(self):
        frame_flock = tk.Frame(self, bd=2, relief=tk.GROOVE)
        frame_flock.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_settings = tk.Label(frame_flock, text="Flock Settings")
        label_flock_settings.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_count = tk.Frame(frame_flock, bd=1, relief=tk.RAISED)
        frame_flock_count.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_count = tk.Label(frame_flock_count, text="Count")
        label_flock_count.pack(side=tk.TOP, padx=5, pady=5)

        text_flock_count = tk.Text(frame_flock_count, height=1, width=2)
        text_flock_count.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_size = tk.Frame(frame_flock, bd=1, relief=tk.RAISED)
        frame_flock_size.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_size = tk.Label(frame_flock_size, text="Size")
        label_flock_size.pack(side=tk.TOP, padx=5, pady=5)

        text_flock_size = tk.Text(frame_flock_size, height=1, width=2)
        text_flock_size.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_default_position = tk.Frame(frame_flock, bd=1, relief=tk.RAISED)
        frame_flock_default_position.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        label_flock_default_position = tk.Label(frame_flock_default_position, text="Default Position")
        label_flock_default_position.pack(side=tk.TOP, padx=5, pady=5)

        frame_flock_default_position_1 = tk.Frame(frame_flock_default_position)
        frame_flock_default_position_1.pack(side=tk.TOP)

        label_flock_default_position_x = tk.Label(frame_flock_default_position_1, text="X: ")
        label_flock_default_position_x.pack(side=tk.LEFT, padx=5, pady=5)

        text_flock_default_position_x = tk.Text(frame_flock_default_position_1, height=1, width=4)
        text_flock_default_position_x.pack(side=tk.LEFT, padx=5, pady=5)

        label_flock_default_position_y = tk.Label(frame_flock_default_position_1, text="Y: ")
        label_flock_default_position_y.pack(side=tk.LEFT, padx=5, pady=5)

        text_flock_default_position_y = tk.Text(frame_flock_default_position_1, height=1, width=4)
        text_flock_default_position_y.pack(side=tk.LEFT, padx=5, pady=5)

        return frame_flock

    #def show(self):
    #    root = tk.Tk()
    #    root.resizable(0, 0)

    #    app = GUI(root)

    #    root.mainloop()

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(0, 0)

    app = GUI(root)

    root.mainloop()