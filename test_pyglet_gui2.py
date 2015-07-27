from pyglet_gui.theme import Theme
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager
import pyglet

window = pyglet.window.Window(640, 480, resizable=True, vsync=True)
batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    batch.draw()
    
theme = Theme({"font": "Lucida Grande",
               "font_size": 12,
               "text_color": [255, 0, 0, 255]}, resources_path='')
label = Label('Hello world')

Manager(label, window=window, theme=theme, batch=batch)
pyglet.app.run()