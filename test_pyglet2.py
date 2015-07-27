import pyglet

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.A:
        print 'The "A" key was pressed.'
    elif symbol == pyglet.window.key.LEFT:
        print 'The left arrow key was pressed.'
    elif symbol == pyglet.window.key.ENTER:
        print 'The enter key was pressed.'

@window.event
def on_draw():
    window.clear()

pyglet.app.run()