import tkinter as tk
from PIL import Image

class Window:
    window: tk.Tk
    spriteSheetPath = '../../assets/cards-spritesheet.png'

    def __init__(self):
        self.window = tk.Tk()
        self.run()

    def run(self):
        self.window.mainloop()

    def readSprites(self):
        spritesheet = Image.open(self.spriteSheetPath)
        