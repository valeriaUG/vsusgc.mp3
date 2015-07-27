# -*- coding: utf-8 -*-

import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
font_name='Consolas', font_size=36,
x=window.width/2, y=window.height/2,
anchor_x='center', anchor_y='center')

#Esto es un decorator. Añade una funcionalidad extra a la función on_draw.
#En este caso, hace que se muestre el texto en la ventana.
@window.event
def on_draw():
    window.clear()
    label.draw()
    
#Si comento esto, la ventana se abre y cierra instantáneamente.
pyglet.app.run()