import src.Gui

class Application:

    def __init__(self):
        self.data=None
        self.gui=src.Gui.GUI()
        self.is_visible=True
        self.data = self.gui.start(self.on_tick,1500)

    def print_console(self):
        print("Hello")

    def on_tick(self):
        self.print_console()
        self.is_visible = not self.is_visible
        #self.gui.set_visible(self.is_visible)

if __name__ == '__main__':
    app = Application()
    if app.data == None:
        print("Hello")

    #gui.set_visible(False)
    #gui.set_visible(True)