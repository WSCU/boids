
import Config as config
import World as world
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import json
import P3
import platform

color_frame_background = 'lightgray'
color_confirm = 'lightgreen'
color_cancel = 'pink'

class Boid_Behavior:

    def __init__(self,perception=0,distance=0,decay=0):
        self.perception_radius=perception
        self.distance_weight=distance
        self.decay_weight=decay

class _Gui_Widget:

    def get_frame(self):
        return self.__frame

    def set_frame(self,value):
        if isinstance(value,tk.Frame):
            self.__frame = value

    def set_enabled(self, is_enabled ,parent=None):
        if parent == None:
            parent=self.get_frame()
        for child in parent.winfo_children():
            #if hasattr(child,'state'):
                #child.configure(state="disabled")
            if isinstance(child,tk.Button) or isinstance(child,tk.Listbox) or isinstance(child, tk.Text):
                if is_enabled:
                    child.configure(state="normal")
                else:
                    child.configure(state="disabled")
            elif isinstance(child,tk.Frame):
                self.set_enabled(is_enabled,child)

class _Widget_Flock(_Gui_Widget):

    def get_flock_size_enabled(self):
        return self.is_flock_size_enabled

    def set_flock_size_enabled(self,is_enabled):
        if is_enabled!=self.is_flock_size_enabled:
            self.set_enabled(is_enabled,self.frame_flock_size)
            self.is_flock_size_enabled = is_enabled

    def get_flock_size(self):
        return int(self.text_flock_size.get(1.0,tk.END))

    def set_flock_size(self,value):
        if isinstance(self.text_flock_size, tk.Text):
            if value == None:
                self.text_flock_size.delete(1.0, tk.END)
                self.text_flock_size.insert(tk.END, 0)
            else:
                self.text_flock_size.delete(1.0, tk.END)
                self.text_flock_size.insert(tk.END, value)

    def flock_size_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Flock):
            self.selected_value.count=self.get_flock_size()

    def get_flock_behavior_enabled(self):
        return self.is_flock_behavior_enabled

    def set_flock_behavior_enabled(self,is_enabled):
        if is_enabled!=self.is_flock_behavior_enabled:
            self.set_enabled(is_enabled,self.frame_flock_behavior)
            self.is_flock_behavior_enabled = is_enabled
                
    def get_flock_behavior_id(self):
        value = int(self.text_flock_behavior.get(1.0,tk.END))
        return value

    def set_flock_behavior_id(self,value):
        if isinstance(self.text_flock_behavior, tk.Text):
            if value == None:
                self.text_flock_behavior.delete(1.0, tk.END)
                self.text_flock_behavior.insert(tk.END, 0)
            else:
                self.text_flock_behavior.delete(1.0, tk.END)
                self.text_flock_behavior.insert(tk.END, value)

    def flock_behavior_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Flock):
            self.selected_value.behavior_id=self.get_flock_behavior_id()

    def get_flock_center_enabled(self):
        return self.is_flock_center_enabled

    def set_flock_center_enabled(self,is_enabled):
        if is_enabled!=self.is_flock_center_enabled:
            self.set_enabled(is_enabled,self.frame_flock_center)
            self.is_flock_center_enabled = is_enabled

    def get_flock_center(self):
        return P3(self.get_flock_center_x(),self.get_flock_center_y(),self.get_flock_center_z())

    def set_flock_center(self,value):
        if isinstance(value,P3.P3):
            self.set_flock_center_x(value.x)
            self.set_flock_center_y(value.y)
            self.set_flock_center_z(value.z)
        else:
            self.set_flock_center_x(0)
            self.set_flock_center_y(0)
            self.set_flock_center_z(0)

    def get_flock_center_x(self):
        return float(self.text_flock_center_x.get(1.0,tk.END))

    def set_flock_center_x(self,value):
        if isinstance(self.text_flock_center_x, tk.Text):
            if value == None:
                self.text_flock_center_x.delete(1.0, tk.END)
                self.text_flock_center_x.insert(tk.END, 0)
            else:
                self.text_flock_center_x.delete(1.0, tk.END)
                self.text_flock_center_x.insert(tk.END, value)

    def flock_center_x_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Flock):
            self.selected_value.center=self.get_flock_center()

    def get_flock_center_y(self):
        return float(self.text_flock_center_y.get(1.0,tk.END))

    def set_flock_center_y(self,value):
        if isinstance(self.text_flock_center_y, tk.Text):
            if value == None:
                self.text_flock_center_y.delete(1.0, tk.END)
                self.text_flock_center_y.insert(tk.END, 0)
            else:
                self.text_flock_center_y.delete(1.0, tk.END)
                self.text_flock_center_y.insert(tk.END, value)

    def flock_center_y_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Flock):
            self.selected_value.center=self.get_flock_center()

    def get_flock_center_z(self):
        return float(self.text_flock_center_z.get(1.0,tk.END))

    def set_flock_center_z(self,value):
        if isinstance(self.text_flock_center_z,tk.Text):
            if value == None:
                self.text_flock_center_z.delete(1.0, tk.END)
                self.text_flock_center_z.insert(tk.END, 0)
            else:
                self.text_flock_center_z.delete(1.0, tk.END)
                self.text_flock_center_z.insert(tk.END, value)

    def flock_center_z_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Flock):
            self.selected_value.center=self.get_flock_center()

    def get_flock_radius_enabled(self):
        return self.is_flock_radius_enabled

    def set_flock_radius_enabled(self,is_enabled):
        if is_enabled!=self.is_flock_radius_enabled:
            self.set_enabled(is_enabled,self.frame_flock_radius)
            self.is_flock_radius_enabled = is_enabled

    def get_flock_radius(self):
        return float(self.text_flock_radius.get(1.0,tk.END))

    def set_flock_radius(self,value):
        if isinstance(self.text_flock_radius, tk.Text):
            if value == None:
                self.text_flock_radius.delete(1.0, tk.END)
                self.text_flock_radius.insert(tk.END, 0)
            else:
                self.text_flock_radius.delete(1.0, tk.END)
                self.text_flock_radius.insert(tk.END, value)

    def flock_radius_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Flock):
            self.selected_value.radius=self.get_flock_radius()

    def add_flock(self,flock):
        if isinstance(flock,config.Config_Flock) and isinstance(self.listbox_flock,tk.Listbox):
            if flock.id not in self.flocks.keys():
                self.flocks[flock.id] = flock
                self.listbox_flock.insert(tk.END,flock.id)
            else:
                self.flocks[flock.id] = flock

    def remove_flock(self,id):
        if id == None:
            return

        if id in self.flocks.keys():
            self.flocks.pop(id,None)

        if isinstance(self.listbox_flock,tk.Listbox):
            self.listbox_flock.delete(self.listbox_flock.get(0,tk.END).index(id))

    def __init__(self,parent):
        if isinstance(parent,tk.Frame):

            self.flocks = {}
            self.frame_flock_size = None
            self.text_flock_size = None
            self.frame_flock_behavior = None
            self.text_flock_behavior = None
            self.frame_flock_center = None
            self.text_flock_center_x = None
            self.text_flock_center_y = None
            self.text_flock_center_z = None
            self.frame_flock_radius = None
            self.text_flock_radius = None
            self.listbox_flock = None

            self.init_frame(parent)

            self.is_flock_size_enabled = None
            self.is_flock_behavior_enabled = None
            self.is_flock_center_enabled = None
            self.is_flock_radius_enabled = None

            self.selected_index = None
            self.selected_value = None

            self.on_behavior_select()

    def init_frame(self,parent):
        frame = tk.Frame(parent, bd=2, relief=tk.GROOVE, bg=color_frame_background)
        frame.pack(side=tk.LEFT, anchor=tk.N, padx=1, pady=1)

        label_flock_settings = tk.Label(frame, text="Flocks", bd=2, relief=tk.GROOVE)
        label_flock_settings.pack(side=tk.TOP, padx=3, pady=3)

        frame_flock_list = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        frame_flock_list.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        frame_flock_list_1 = tk.Frame(frame_flock_list)
        frame_flock_list_1.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N)

        label_flock = tk.Label(frame_flock_list_1, text="Flock")
        label_flock.pack(side=tk.TOP, padx=1, pady=1)

        listbox_flocks_scrollbar = tk.Scrollbar(frame_flock_list_1, orient=tk.VERTICAL)
        listbox_flocks_scrollbar.pack(side=tk.RIGHT, )

        self.listbox_flock = tk.Listbox( \
            frame_flock_list_1, \
            yscrollcommand=listbox_flocks_scrollbar.set, \
            name='listbox_flocks', selectmode=tk.SINGLE, height=3, width=6, bd=2, relief=tk.GROOVE)
        listbox_flocks_scrollbar.config(command=self.listbox_flock.yview)

        self.listbox_flock.pack(side=tk.TOP)
        self.listbox_flock.bind('<<ListboxSelect>>', self.on_behavior_select)

        frame_flock_list_2 = tk.Frame(frame_flock_list)
        frame_flock_list_2.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.S)

        button_remove_flock = tk.Button(frame_flock_list_2, text="Remove", bg=color_cancel, bd=2, relief=tk.GROOVE, command=self.flock_remove_onclick)
        button_remove_flock.pack(side=tk.BOTTOM, fill=tk.BOTH)

        button_add_flock = tk.Button(frame_flock_list_2, text="Add", bg=color_confirm, bd=2, relief=tk.GROOVE, command=self.flock_add_onclick)
        button_add_flock.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.frame_flock_size = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_flock_size.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_flock_size = tk.Label(self.frame_flock_size, text="Size")
        label_flock_size.pack(side=tk.TOP, padx=3, pady=3)

        self.text_flock_size = tk.Text(self.frame_flock_size, height=1, width=2, bd=2, relief=tk.GROOVE)
        self.text_flock_size.pack(side=tk.TOP, padx=3, pady=3)
        self.text_flock_size.bind('<FocusOut>',self.flock_size_onfocusout)

        self.frame_flock_behavior = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_flock_behavior.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_flock_behavior = tk.Label(self.frame_flock_behavior, text="Behavior")
        label_flock_behavior.pack(side=tk.TOP, padx=3, pady=3)

        self.text_flock_behavior = tk.Text(self.frame_flock_behavior, height=1, width=2, bd=2, relief=tk.GROOVE)
        self.text_flock_behavior.pack(side=tk.TOP, padx=3, pady=3)
        self.text_flock_behavior.bind('<FocusOut>', self.flock_behavior_onfocusout)

        self.frame_flock_center = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_flock_center.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_flock_center = tk.Label(self.frame_flock_center, text="Center")
        label_flock_center.pack(side=tk.TOP, padx=3, pady=3)

        frame_flock_center_1 = tk.Frame(self.frame_flock_center)
        frame_flock_center_1.pack(side=tk.TOP, fill=tk.Y)

        label_flock_center_x = tk.Label(frame_flock_center_1, text="X: ")
        label_flock_center_x.pack(side=tk.LEFT, padx=3, pady=3)

        self.text_flock_center_x = tk.Text(frame_flock_center_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        self.text_flock_center_x.pack(side=tk.LEFT, padx=3, pady=3)
        self.text_flock_center_x.bind('<FocusOut>', self.flock_center_x_onfocusout)

        label_flock_center_y = tk.Label(frame_flock_center_1, text="Y: ")
        label_flock_center_y.pack(side=tk.LEFT, padx=3, pady=3)

        self.text_flock_center_y = tk.Text(frame_flock_center_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        self.text_flock_center_y.pack(side=tk.LEFT, padx=3, pady=3)
        self.text_flock_center_y.bind('<FocusOut>', self.flock_center_y_onfocusout)

        label_flock_center_z = tk.Label(frame_flock_center_1, text="Z: ")
        label_flock_center_z.pack(side=tk.LEFT, padx=3, pady=3)

        self.text_flock_center_z = tk.Text(frame_flock_center_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        self.text_flock_center_z.pack(side=tk.LEFT, padx=3, pady=3)
        self.text_flock_center_z.bind('<FocusOut>', self.flock_center_z_onfocusout)

        self.frame_flock_radius = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_flock_radius.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_flock_radius = tk.Label(self.frame_flock_radius, text="Radius")
        label_flock_radius.pack(side=tk.TOP, padx=3, pady=3)

        self.text_flock_radius = tk.Text(self.frame_flock_radius, height=1, width=2, bd=2, relief=tk.GROOVE)
        self.text_flock_radius.pack(side=tk.TOP, padx=3, pady=3)
        self.text_flock_radius.bind('<FocusOut>', self.flock_radius_onfocusout)

        self.set_frame(frame)

    def on_behavior_select(self, evt=None):
        w = self.listbox_flock
        if (len(w.curselection())>0):
            self.selected_index = int(w.curselection()[0])
            self.selected_value = self.flocks[w.get(self.selected_index)]
            self.set_flock_size_enabled(True)
            self.set_flock_behavior_enabled(True)
            self.set_flock_center_enabled(True)
            self.set_flock_radius_enabled(True)
            self.update_selection()
        else:
            self.selected_index = None
            self.selected_value = None
            self.update_selection()
            self.set_flock_size_enabled(False)
            self.set_flock_behavior_enabled(False)
            self.set_flock_center_enabled(False)
            self.set_flock_radius_enabled(False)

    def update_selection(self):
        if isinstance(self.selected_value,config.Config_Flock):
            self.set_flock_center(self.selected_value.center)
            self.set_flock_radius(self.selected_value.radius)
            self.set_flock_behavior_id(self.selected_value.behavior_id)

            size = 0
            if self.selected_value.boids != None:
                if isinstance(self.selected_value.boids,config.Config_Boids):
                    self.set_flock_behavior(self.selected_value.boids.behavior)
                    size=self.selected_value.boids.count
                elif isinstance(self.selected_value.boids,list):
                    size = len(self.selected_value.boids)
                    self.set_flock_behavior(None)
            else:
                size=self.selected_value.count

            self.set_flock_size(size)

        else:
            self.set_flock_center(None)
            self.set_flock_radius(None)
            self.set_flock_size(None)
            self.set_flock_behavior_id(None)

    def flock_add_onclick(self):
        size = len(self.flocks)
        value = config.Config_Flock(size)
        self.add_flock(value)
        #self.on_behavior_select()

    def flock_remove_onclick(self):
        if isinstance(self.listbox_flock,tk.Listbox):
            id = self.listbox_flock.get(self.listbox_flock.curselection())
            self.remove_flock(id)
            self.on_behavior_select()

    def to_config(self):
        return self.flocks

    def from_config(self,data):
        if data != None:
            for key in data:
                if isinstance(data[key],config.Config_Flock):
                    self.add_flock(data[key])

class _Widget_Behavior(_Gui_Widget):
    def get_behavior_neighbor_enabled(self):
        return self.is_behavior_neighbor_enabled

    def set_behavior_neighbor_enabled(self, is_enabled):
        if is_enabled != self.is_behavior_neighbor_enabled:
            self.set_enabled(is_enabled, self.frame_behavior_neighbor)
            self.is_behavior_neighbor_enabled = is_enabled

    def get_behavior_neighbor(self):
        return float(self.text_behavior_neighbor.get(1.0, tk.END))

    def set_behavior_neighbor(self, value):
        if isinstance(self.text_behavior_neighbor, tk.Text):
            if value == None:
                self.text_behavior_neighbor.delete(1.0, tk.END)
                self.text_behavior_neighbor.insert(tk.END, 0)
            else:
                self.text_behavior_neighbor.delete(1.0, tk.END)
                self.text_behavior_neighbor.insert(tk.END, value)

    def behavior_neighbor_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Behavior):
            self.selected_value.neighbor_weight=self.get_behavior_neighbor()

    def get_behavior_center_enabled(self):
        return self.is_behavior_center_enabled

    def set_behavior_center_enabled(self, is_enabled):
        if is_enabled != self.is_behavior_center_enabled:
            self.set_enabled(is_enabled, self.frame_behavior_center)
            self.is_behavior_center_enabled = is_enabled

    def get_behavior_center(self):
        return self.text_behavior_center.get(1.0, tk.END)

    def set_behavior_center(self, value):
        if isinstance(self.text_behavior_center, tk.Text):
            if value == None:
                self.text_behavior_center.delete(1.0, tk.END)
                self.text_behavior_center.insert(tk.END, 0)
            else:
                self.text_behavior_center.delete(1.0, tk.END)
                self.text_behavior_center.insert(tk.END, value)

    def behavior_center_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Behavior):
            self.selected_value.center_weight=self.get_behavior_center()

    def get_behavior_direction_enabled(self):
        return self.is_behavior_direction_enabled

    def set_behavior_direction_enabled(self, is_enabled):
        if is_enabled != self.is_behavior_direction_enabled:
            self.set_enabled(is_enabled, self.frame_behavior_direction)
            self.is_behavior_direction_enabled = is_enabled

    def get_behavior_direction(self):
        return self.text_behavior_direction.get(1.0, tk.END)

    def set_behavior_direction(self, value):
        if isinstance(self.text_behavior_direction, tk.Text):
            if value == None:
                self.text_behavior_direction.delete(1.0, tk.END)
                self.text_behavior_direction.insert(tk.END, 0)
            else:
                self.text_behavior_direction.delete(1.0, tk.END)
                self.text_behavior_direction.insert(tk.END, value)

    def behavior_direction_onfocusout(self,evt=None):
        if self.selected_value!=None and isinstance(self.selected_value,config.Config_Behavior):
            self.selected_value.direction_weight=self.get_behavior_direction()

    def add_behavior(self, behavior):
        if isinstance(behavior, config.Config_Behavior) and isinstance(self.listbox_behaviors, tk.Listbox):
            if behavior.id not in self.behaviors.keys():
                self.behaviors[behavior.id] = behavior
                self.listbox_behaviors.insert(tk.END, behavior.id)
            else:
                self.behaviors[behavior.id] = behavior

    def remove_behavior(self, id):
        if id == None:
            return

        if id in self.behaviors.keys():
            self.behaviors.pop(id, None)

        if isinstance(self.listbox_behavior, tk.Listbox):
            self.listbox_behavior.delete(self.listbox_behavior.get(0, tk.END).index(id))

    def __init__(self, parent):
        if isinstance(parent, tk.Frame):
            self.behaviors = {}

            self.listbox_behaviors = None
            self.frame_behavior_neighbor = None
            self.text_behavior_neighbor = None
            self.frame_behavior_center = None
            self.text_behavior_center = None
            self.frame_behavior_direction = None
            self.text_behavior_direction = None

            self.init_frame(parent)

            self.is_behavior_neighbor_enabled = None
            self.is_behavior_direction_enabled = None
            self.is_behavior_center_enabled = None

            self.selected_index = None
            self.selected_value = None

            self.on_behavior_select()

    def init_frame(self,parent):
        frame = tk.Frame(parent, bd=2, relief=tk.GROOVE, bg=color_frame_background)
        frame.pack(side=tk.LEFT, anchor=tk.N, padx=1, pady=1)

        label_behavior_settings = tk.Label(frame, text="Behaviors", bd=2, relief=tk.GROOVE)
        label_behavior_settings.pack(side=tk.TOP, padx=3, pady=3)

        frame_behavior_list = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        frame_behavior_list.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        frame_behavior_list_1 = tk.Frame(frame_behavior_list)
        frame_behavior_list_1.pack(side=tk.LEFT, padx=1)

        label_behavior = tk.Label(frame_behavior_list_1, text="Behavior")
        label_behavior.pack(side=tk.TOP, padx=3, pady=3)

        listbox_behaviors_scrollbar = tk.Scrollbar(frame_behavior_list_1, orient=tk.VERTICAL)
        self.listbox_behaviors = tk.Listbox( \
            frame_behavior_list_1, \
            yscrollcommand=listbox_behaviors_scrollbar.set, \
            name='listbox_behaviors', height=3, width=8, bd=2, relief=tk.GROOVE)
        listbox_behaviors_scrollbar.config(command=self.listbox_behaviors.yview)
        listbox_behaviors_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_behaviors.pack(side=tk.TOP, fill=tk.Y)
        self.listbox_behaviors.bind('<<ListboxSelect>>', self.on_behavior_select)

        frame_behavior_list_2 = tk.Frame(frame_behavior_list)
        frame_behavior_list_2.pack(side=tk.LEFT, fill=tk.Y, padx=1, anchor=tk.S)

        button_remove_behavior = tk.Button(frame_behavior_list_2, text="Remove", bg=color_cancel, bd=2, relief=tk.GROOVE, command=self.behavior_remove_onclick)
        button_remove_behavior.pack(side=tk.BOTTOM, fill=tk.BOTH)

        button_add_behavior = tk.Button(frame_behavior_list_2, text="Add", bg=color_confirm, bd=2, relief=tk.GROOVE, command=self.behavior_add_onclick)
        button_add_behavior.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.frame_behavior_neighbor = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_behavior_neighbor.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_behavior_neighbor = tk.Label(self.frame_behavior_neighbor, text="Neighbor")
        label_behavior_neighbor.pack(side=tk.TOP, padx=3, pady=3)

        self.text_behavior_neighbor = tk.Text(self.frame_behavior_neighbor, height=1, width=2, bd=2, relief=tk.GROOVE)
        self.text_behavior_neighbor.pack(side=tk.TOP, padx=3, pady=3)
        self.text_behavior_neighbor.bind('<FocusOut>', self.behavior_neighbor_onfocusout)

        self.frame_behavior_center = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_behavior_center.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_behavior_center = tk.Label(self.frame_behavior_center, text="Center")
        label_behavior_center.pack(side=tk.TOP, padx=3, pady=3)

        self.text_behavior_center = tk.Text(self.frame_behavior_center, height=1, width=2, bd=2, relief=tk.GROOVE)
        self.text_behavior_center.pack(side=tk.TOP, padx=3, pady=3)
        self.text_behavior_center.bind('<FocusOut>', self.behavior_center_onfocusout)

        self.frame_behavior_direction = tk.Frame(frame, bd=2, relief=tk.GROOVE)
        self.frame_behavior_direction.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_behavior_direction = tk.Label(self.frame_behavior_direction, text="Direction")
        label_behavior_direction.pack(side=tk.TOP, padx=3, pady=3)

        self.text_behavior_direction = tk.Text(self.frame_behavior_direction, height=1, width=2, bd=2, relief=tk.GROOVE)
        self.text_behavior_direction.pack(side=tk.TOP, padx=3, pady=3)
        self.text_behavior_direction.bind('<FocusOut>', self.behavior_direction_onfocusout)

        self.set_frame(frame)

    def on_behavior_select(self, evt=None):
        w = self.listbox_behaviors
        if (len(w.curselection())>0):
            self.selected_index = int(w.curselection()[0])
            self.selected_value = self.behaviors[w.get(self.selected_index)]
            self.set_behavior_center_enabled(True)
            self.set_behavior_neighbor(True)
            self.set_behavior_direction_enabled(True)
            self.update_selection()
        else:
            self.selected_index = None
            self.selected_value = None
            self.update_selection()
            self.set_behavior_center_enabled(False)
            self.set_behavior_neighbor(False)
            self.set_behavior_direction_enabled(False)

    def update_selection(self):
        if isinstance(self.selected_value,config.Config_Behavior):
            self.set_behavior_center(self.selected_value.center_weight)
            self.set_behavior_direction(self.selected_value.direction_weight)
            self.set_behavior_neighbor(self.selected_value.neighbor_weight)

        else:
            self.set_behavior_center(None)
            self.set_behavior_direction(None)
            self.set_behavior_neighbor(None)

    def behavior_add_onclick(self):
        size = len(self.behaviors)
        value = config.Config_Behavior(size)
        self.add_behavior(value)
        #self.on_behavior_select()

    def behavior_remove_onclick(self):
        if isinstance(self.listbox_behaviors,tk.Listbox):
            id = self.listbox_behaviors.get(self.listbox_behaviors.curselection())
            self.remove_behavior(id)
            self.on_behavior_select()

    def to_config(self):
        return self.behaviors

    def from_config(self,data):
        if data != None:
            for key in data:
                if isinstance(data[key],config.Config_Behavior):
                    self.add_behavior(data[key])

class _Widget_Boid(_Gui_Widget):

    def __init__(self,parent):
        if isinstance(parent,tk.Frame):
            self.__frame = self.init_frame(parent)

    def init_frame(self,parent):
        frame_boid = tk.Frame(parent, bd=2, relief=tk.GROOVE, bg=color_frame_background)
        frame_boid.pack(side=tk.LEFT, anchor=tk.N, padx=1, pady=1)

        label_boid_settings = tk.Label(frame_boid, text="Boids", bd=2, relief=tk.GROOVE)
        label_boid_settings.pack(side=tk.TOP, padx=3, pady=3)

        frame_boid_list = tk.Frame(frame_boid, bd=2, relief=tk.GROOVE)
        frame_boid_list.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        frame_boid_list_1 = tk.Frame(frame_boid_list)
        frame_boid_list_1.pack(side=tk.LEFT, fill=tk.Y, padx=1)

        label_boid = tk.Label(frame_boid_list_1, text="Boid")
        label_boid.pack(side=tk.TOP, padx=3, pady=3)

        listbox_boids_scrollbar = tk.Scrollbar(frame_boid_list_1, orient=tk.VERTICAL)
        listbox_boids = tk.Listbox( \
            frame_boid_list_1, \
            yscrollcommand=listbox_boids_scrollbar.set, \
            name='listbox_boids', height=3, width=6, bd=2, relief=tk.GROOVE)
        listbox_boids_scrollbar.config(command=listbox_boids.yview)
        listbox_boids_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox_boids.pack(side=tk.TOP, fill=tk.Y)
        listbox_boids.bind('<<ListboxSelect>>', GUI.on_boid_select)

        #frame_boid_list_2 = tk.Frame(frame_boid_list)
        #frame_boid_list_2.pack(side=tk.LEFT, fill=tk.Y, padx=1, anchor=tk.S)

        #button_remove_boid = tk.Button(frame_boid_list_2, text="Remove", bg=color_cancel, bd=2, relief=tk.GROOVE)
        #button_remove_boid.pack(side=tk.BOTTOM, fill=tk.BOTH)

        #button_add_boid = tk.Button(frame_boid_list_2, text="Add", bg=color_confirm, bd=2, relief=tk.GROOVE)
        #button_add_boid.pack(side=tk.BOTTOM, fill=tk.BOTH)

        frame_boid_id = tk.Frame(frame_boid, bd=2, relief=tk.GROOVE)
        frame_boid_id.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_boid_id = tk.Label(frame_boid_id, text="Id")
        label_boid_id.pack(side=tk.TOP, padx=3, pady=3)

        text_boid_id = tk.Text(frame_boid_id, height=1, width=2, bd=2, relief=tk.GROOVE)
        text_boid_id.pack(side=tk.TOP, padx=3, pady=3)

        frame_boid_velocity_max = tk.Frame(frame_boid, bd=2, relief=tk.GROOVE)
        frame_boid_velocity_max.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_boid_velocity_max = tk.Label(frame_boid_velocity_max, text="Max Velocity")
        label_boid_velocity_max.pack(side=tk.TOP, padx=3, pady=3)

        text_boid_velocity_max = tk.Text(frame_boid_velocity_max, height=1, width=2, bd=2, relief=tk.GROOVE)
        text_boid_velocity_max.pack(side=tk.TOP, padx=3, pady=3)

        frame_boid_velocity = tk.Frame(frame_boid, bd=2, relief=tk.GROOVE)
        frame_boid_velocity.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_boid_velocity = tk.Label(frame_boid_velocity, text="Velocity")
        label_boid_velocity.pack(side=tk.TOP, padx=3, pady=3)

        frame_boid_velocity_1 = tk.Frame(frame_boid_velocity)
        frame_boid_velocity_1.pack(side=tk.TOP, fill=tk.Y)

        label_boid_velocity_x = tk.Label(frame_boid_velocity_1, text="X: ")
        label_boid_velocity_x.pack(side=tk.LEFT, padx=3, pady=3)

        text_boid_velocity_x = tk.Text(frame_boid_velocity_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_velocity_x.pack(side=tk.LEFT, padx=3, pady=3)

        label_boid_velocity_y = tk.Label(frame_boid_velocity_1, text="Y: ")
        label_boid_velocity_y.pack(side=tk.LEFT, padx=3, pady=3)

        text_boid_velocity_y = tk.Text(frame_boid_velocity_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_velocity_y.pack(side=tk.LEFT, padx=3, pady=3)

        label_boid_velocity_z = tk.Label(frame_boid_velocity_1, text="Z: ")
        label_boid_velocity_z.pack(side=tk.LEFT, padx=3, pady=3)

        text_boid_velocity_z = tk.Text(frame_boid_velocity_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_velocity_z.pack(side=tk.LEFT, padx=3, pady=3)

        frame_boid_position = tk.Frame(frame_boid, bd=2, relief=tk.GROOVE)
        frame_boid_position.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_boid_position = tk.Label(frame_boid_position, text="Position")
        label_boid_position.pack(side=tk.TOP, padx=3, pady=3)

        frame_boid_position_1 = tk.Frame(frame_boid_position)
        frame_boid_position_1.pack(side=tk.TOP, fill=tk.Y)

        label_boid_position_x = tk.Label(frame_boid_position_1, text="X: ")
        label_boid_position_x.pack(side=tk.LEFT, padx=3, pady=3)

        text_boid_position_x = tk.Text(frame_boid_position_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_position_x.pack(side=tk.LEFT, padx=3, pady=3)

        label_boid_position_y = tk.Label(frame_boid_position_1, text="Y: ")
        label_boid_position_y.pack(side=tk.LEFT, padx=3, pady=3)

        text_boid_position_y = tk.Text(frame_boid_position_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_position_y.pack(side=tk.LEFT, padx=3, pady=3)

        label_boid_position_z = tk.Label(frame_boid_position_1, text="Z: ")
        label_boid_position_z.pack(side=tk.LEFT, padx=3, pady=3)

        text_boid_position_z = tk.Text(frame_boid_position_1, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_position_z.pack(side=tk.LEFT, padx=3, pady=3)

        frame_boid_behavior_list = tk.Frame(frame_boid, bd=2, relief=tk.GROOVE)
        frame_boid_behavior_list.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=3, pady=3)

        label_boid = tk.Label(frame_boid_behavior_list, text="Behavior")
        label_boid.pack(side=tk.TOP, padx=3, pady=3)
        
        text_boid_behavior = tk.Text(frame_boid_behavior_list, height=1, width=4, bd=2, relief=tk.GROOVE)
        text_boid_behavior.pack(side=tk.TOP,padx=3,pady=3)

        #listbox_boid_behavior_scrollbar = tk.Scrollbar(frame_boid_behavior_list, orient=tk.VERTICAL)
        #listbox_boid_behavior = tk.Listbox( \
        #    frame_boid_behavior_list, \
        #    yscrollcommand=listbox_boid_behavior_scrollbar.set, \
        #    name='listbox_boid_behavior', height=3, width=8, bd=2, relief=tk.GROOVE)
        #listbox_boid_behavior_scrollbar.config(command=listbox_boid_behavior.yview)
        #listbox_boid_behavior_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #listbox_boid_behavior.pack(side=tk.TOP, fill=tk.Y)

        return frame_boid

class _Widget_Commands(_Gui_Widget):
    def get_frame(self):
        return self.__frame

    def __init__(self,parent, load_onclick, save_onclick,saveas_onclick, startstop_onclick):
        if isinstance(parent,tk.Frame):
            self.__frame = self.init_frame(parent,load_onclick,save_onclick,saveas_onclick,startstop_onclick)

    def init_frame(self,parent, load_onclick, save_onclick,saveas_onclick, startstop_onclick):
        frame_commands = tk.Frame(parent, bd=2, relief=tk.GROOVE, bg=color_frame_background)
        frame_commands.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.N, padx=1, pady=1)

        label_commands = tk.Label(frame_commands, text="Commands", bd=2, relief=tk.GROOVE)
        label_commands.pack(side=tk.TOP, padx=3, pady=3)

        frame_command_config = tk.Frame(frame_commands, bd=2, relief=tk.GROOVE)
        frame_command_config.pack(side=tk.LEFT, padx=1, pady=1)

        button_load_config = tk.Button(frame_command_config, text="Load Config", bd=2, relief=tk.GROOVE, command=load_onclick)
        button_load_config.pack(side=tk.TOP, fill=tk.X)

        button_save_config = tk.Button(frame_command_config, text="Save Config", bd=2, relief=tk.GROOVE, command=save_onclick)
        button_save_config.pack(side=tk.TOP, fill=tk.X)

        button_saveas_config = tk.Button(frame_command_config, text="Save Config As", bd=2, relief=tk.GROOVE, command=saveas_onclick)
        button_saveas_config.pack(side=tk.TOP, fill=tk.X)

        frame_simulation = tk.Frame(frame_commands, bd=2, relief=tk.GROOVE)
        frame_simulation.pack(side=tk.LEFT, fill=tk.Y, padx=1, pady=1)

        button_simulation_toggle = tk.Button(frame_simulation, text="Start/Stop Simulation", bd=2, relief=tk.GROOVE,command=startstop_onclick)
        button_simulation_toggle.pack(fill=tk.BOTH, expand=tk.YES)

        return frame_commands

class GUI(tk.Frame):

    def get_os_title_height(self):
        p = platform.system()
        if str(p).upper() == 'WINDOWS':
            return 30
        else:
            return 20

    def get_master(self):
        return self.master

    def get_world_config(self):
        screen = config.Config_Screen(self.world_x,self.world_y,self.sw,self.sh)
        data = config.Config_World(
            None,
            self.__widget_flock.to_config(),
            self.__widget_behavior.to_config(),
            screen
        )
        return data

    def get_world_json(self):
        data=self.get_world_config()
        value = data.to_dict()
        return value

    def set_world_config(self,data):
        if data!=None and isinstance(data,config.Config_World):
            self.__widget_flock.from_config(data.flocks)
            self.__widget_behavior.from_config(data.behaviors)

    def set_tick_wait(self,wait):
        self.tick_wait=wait

    def set_tick_method(self,method):
        self.tick_method=method

    def tick(self):
        if self.tick_method!=None:
            self.tick_method()
        self.master.after(self.tick_wait, self.tick)

    def __init__(self):

        self.master = tk.Tk()
        self.master.resizable(0, 0)
        self.default_height = 120

        self.tick_wait = world.World.tick_time
        self.tick_method = None
        self.file_path = None

        tk.Frame.__init__(self, self.master)
        #self.config = Config()
        self.init_ui()

        self.master.after(self.tick_wait, self.tick)
        self.master.mainloop()

    def init_ui(self):
        self.init_position()
        self.init_controls()

    def init_position(self):
        self.master.title("Python Boids")
        self.pack(fill=tk.BOTH, expand=True)
        self.app_window = tk.Toplevel(self.master)
        self.app_frame = tk.Frame(self.app_window)
        self.app_window.overrideredirect(True)
        self.app_frame.pack()

        self.sw = self.master.winfo_screenwidth()
        self.sh = self.master.winfo_screenheight()-(self.default_height + self.get_os_title_height()*2+30)
        self.ui_x = -7
        self.ui_y = 0
        self.world_x=self.ui_x
        self.world_y=self.ui_y+self.default_height+60

        #self.config.set_size((sw, sh-self.default_height))

        self.master.geometry('%dx%d+%d+%d' % (self.sw, self.default_height, self.ui_x, self.ui_y))

    def init_controls(self):

        self.__widget_flock = _Widget_Flock(self)
        self.__widget_behavior = _Widget_Behavior(self)
        #self.__widget_boid = _Widget_Boid(self)
        self.__widget_commands = _Widget_Commands(self,self.load_onclick,self.save_onclick,self.saveas_onclick,self.start_onclick)

        #self.__widget_flock.set_enabled(False)
        #self.__widget_behavior.set_enabled(False)
        #self.__widget_commands.set_enabled(False)

        #if self.sw>=1920:
            #self.init_full_gui()
        #else:
            #self.init_compact_gui()

    def init_full_gui(self):
        self.init_flock_frame(self)
        self.init_behavior_frame(self)
        self.init_boid_frame(self)
        self.init_command_frame(self)

    def init_compact_gui(self):
        self.init_full_gui()

        #button_toggle_flock = tk.Button()

        #frame_flock = self.init_flock_frame(self)
        #frame_behavior = self.init_behavior_frame(self)
        #frame_boid = self.init_boid_frame(self)

        #self.set_frame_visible(frame_behavior,False)

    def set_frame_visible(self,frame,is_visible):
        if isinstance(frame,tk.Frame) and isinstance(is_visible,bool):
            if is_visible:
                frame.grid()
            else:
                frame.pack_forget()

    def set_visible(self, value):
        if isinstance(value, bool):
            if value == True:
                self.master.update()
                self.master.deiconify()
            else:
                self.master.withdraw()

    def start_onclick(self,evt=None):
        value = self.get_world_config()
        self.world = world.World(value,self)
        return True

    def load_onclick(self,evt=None):
        filename=askopenfilename()
        if filename!=None:
            self.file_path=filename
            self.read_json()

    def save_onclick(self,evt=None):
        if self.file_path!=None:
            self.save_json()
        else:
            self.saveas_onclick()

    def saveas_onclick(self,evt=None):
        filename = asksaveasfilename()
        if filename!=None:
            self.file_path=filename
            self.save_json()

    def read_json(self):
        if self.file_path != None:
            with open(self.file_path,'r') as in_file:
                data=config.Config_World.from_dict(json.loads(in_file.readlines()[0]))
                self.set_world_config(data)

    def save_json(self):
        if self.file_path!=None:
            data = self.get_world_config()
            value = json.dumps(data.to_dict())
            #for key in data:
            #    if value!="":
            #        value+="\n"
            #    value += json.dumps(data.get(key).to_dict())

            if value!="":
                with open(self.file_path, 'w') as out_file:
                    out_file.write(value)

            #config.behaviors=None

if __name__=='__main__':
    app = GUI()
    #app.start()
